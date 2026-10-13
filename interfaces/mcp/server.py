"""Minimal JSON-RPC MCP Alpha surface."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS = [('analyze_chapter','Analyze a chapter.'),('check_continuity','Check continuity.'),('get_character','Read a character.'),('get_timeline','Read timeline.'),('search_knowledge','Search knowledge.'),('evaluate_scene','Evaluate a scene.'),('generate_scene','Generate a scene with Creator Mode.'),('rewrite_scene','Rewrite a scene with Creator Mode.'),('update_memory','Commit confirmed memory proposal.'),('get_project_status','Read project status.')]
RESOURCES = ['novelos://project/current','novelos://character/all','novelos://timeline/current','novelos://world/rules','novelos://writing/state']
PROMPTS = ['novelos-review-chapter','novelos-plan-next-chapter','novelos-character-analysis','novelos-write-scene','novelos-revise-scene']

def storage(name):
    try: return json.loads((ROOT/'memory'/'storage'/f'{name}.json').read_text(encoding='utf-8'))
    except (FileNotFoundError,json.JSONDecodeError): return []

def response(request_id, payload=None, error=None):
    result = {'jsonrpc':'2.0','id':request_id}
    if error:
        result['error'] = {'code':-32000,'message':error}
    else:
        result['result'] = payload
    return result

def call_tool(name, args):
    if name == 'get_character': return storage('character')
    if name == 'get_timeline': return storage('timeline')
    if name == 'get_project_status':
        state = storage('novel_state'); return {'mode':'editor','story_phase':state.get('story_phase','setup') if isinstance(state,dict) else 'setup'}
    if name == 'search_knowledge': return {'query':args.get('query',''),'matches':[],'status':'shared-core-search-contract'}
    if name == 'update_memory' and not args.get('confirm'): return {'status':'proposal','requires_confirmation':True,'proposal':args.get('proposal',{})}
    if name in ('generate_scene','rewrite_scene') and not (args.get('mode') == 'creator' and args.get('confirm')): return {'status':'blocked','reason':'Creator Mode and explicit confirmation are required'}
    return {'status':'queued','tool':name,'mode':args.get('mode','editor'),'note':'Runtime adapter dispatches this tool to shared Core.'}

def dispatch(request):
    method, request_id, params = request.get('method'), request.get('id'), request.get('params',{})
    if method == 'initialize': return response(request_id, {'protocolVersion':'2025-06-18','capabilities':{'tools':{},'resources':{},'prompts':{}},'serverInfo':{'name':'novelos-mcp','version':'3.10.1'}})
    if method == 'tools/list': return response(request_id, {'tools':[{'name':name,'description':description,'inputSchema':{'type':'object'}} for name,description in TOOLS]})
    if method == 'resources/list': return response(request_id, {'resources':[{'uri':uri,'name':uri.rsplit('/',1)[-1]} for uri in RESOURCES]})
    if method == 'prompts/list': return response(request_id, {'prompts':[{'name':name} for name in PROMPTS]})
    if method == 'tools/call': return response(request_id, {'content':[{'type':'text','text':json.dumps(call_tool(params.get('name'),params.get('arguments',{})),ensure_ascii=False)}]})
    if method == 'resources/read': return response(request_id, {'contents':[{'uri':params.get('uri'),'mimeType':'application/json','text':json.dumps({'uri':params.get('uri'),'status':'shared-core-resource'},ensure_ascii=False)}]})
    if method == 'prompts/get': return response(request_id, {'description':'NovelOS workflow prompt','messages':[{'role':'user','content':{'type':'text','text':'Run '+str(params.get('name'))+' through Editor Mode with evidence and confirmation gates.'}}]})
    return response(request_id,error='unsupported method: '+str(method))

if __name__ == '__main__':
    for line in sys.stdin:
        if line.strip(): print(json.dumps(dispatch(json.loads(line)),ensure_ascii=False),flush=True)
