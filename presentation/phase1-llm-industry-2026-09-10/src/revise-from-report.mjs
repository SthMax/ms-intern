import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {PresentationFile,FileBlob} from '@oai/artifact-tool';

const WS=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const REPO=path.resolve(WS,'../..');
const SKILL='/Users/sthmax/.codex/plugins/cache/openai-primary-runtime/presentations/26.905.11957/skills/presentations';
const PYTHON='/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3';
process.env.RUNTIME_NODE_MODULES='/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
process.env.RUNTIME_NODE=process.execPath;process.env.RUNTIME_PYTHON=PYTHON;
const SOURCE=path.join(WS,'output/fund-llm-industry-2026-09-10-final.pptx');
const OUT=path.join(WS,'output',process.env.DECK_FILENAME??'fund-llm-industry-2026-09-11.pptx');
const TMP=path.join(WS,'.build');
const {resolvePresentationFont,finalizePresentation}=await import(pathToFileURL(path.join(SKILL,'container_tools/artifact_tool_utils.mjs')).href);
const font=resolvePresentationFont({fontFamily:'Heiti SC'});
const C={navy:'#19374D',teal:'#008C83',ink:'#253C4A',muted:'#566975',gray:'#CBD5DA',white:'#FFFFFF'};
const reportDir=path.join(REPO,'reports/phase1-llm-industry-2026-09-09');
const refs=JSON.parse(await fs.readFile(path.join(reportDir,'data/source-manifest.json'),'utf8'));
const refMap=Object.fromEntries(refs.map(x=>[x.id,x]));
const p=await PresentationFile.importPptx(await FileBlob.load(SOURCE));
const inspected=await p.inspect({kind:'slide,textbox,table,chart,image,layout',maxChars:220000});
const records=inspected.ndjson.split('\n').filter(Boolean).map(x=>JSON.parse(x));
const original=records.filter(x=>x.kind==='slide').sort((a,b)=>a.slide-b.slide).map(x=>p.resolve(x.id));
if(original.length!==24)throw new Error('Expected original 24-slide deck');
// Duplicate existing slides before editing, preserving the imported masters and layouts.
const extra={quant:original[3].duplicate(),tools:original[23].duplicate(),mentor:original[21].duplicate()};
const seq=[1,4,5,2,22,6,7,9,8,10,11,'quant',13,23,'tools',15,16,17,18,3,19,20,21,'mentor',14,12,24];
const ordered=seq.map(n=>typeof n==='number'?original[n-1]:extra[n]);
ordered.forEach((s,i)=>s.moveTo(i));
const coverage=[],tableOwners=[],chartOwners=[];
function text(s,value,x,y,w,h,size=29,color=C.ink,bold=false,align='left',existing=null){
 const t=existing??s.shapes.add({geometry:'textbox',name:`copy-${coverage.length}-${String(value).slice(0,15)}`,position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 t.frame={left:x,top:y,width:w,height:h};t.text=value;t.text.style={typeface:font,fontSize:size,color,bold,alignment:align,verticalAlignment:'top',autoFit:'none',wrap:'square',insets:{top:0,bottom:0,left:0,right:0}};return t;
}
function page(i,title,{sub='',foot='',footY=646,keepTable=false,keepChart=false,keepImage=false}={}){
 const s=ordered[i-1];const shapes=[...s.shapes.items];
 const titleObj=shapes.find(t=>t.frame.top===43)||shapes.find(t=>t.frame.top<120);
 const numberObj=shapes.find(t=>t.frame.top>=670&&t.frame.left>1100);
 for(const t of shapes)if(t!==titleObj&&t!==numberObj)t.delete();
 if(!keepTable)for(const t of [...s.tables.items])s.tables.deleteById(t.id);
 if(!keepImage)for(const im of [...s.images.items])im.delete();
 if(s.charts.items.length&&!keepChart)throw new Error('Chart must be preserved');
 s.background.fill=C.white;
 text(s,title,64,43,1152,78,44,C.navy,true,'left',titleObj);
 text(s,String(i).padStart(2,'0'),1190,672,34,28,17,C.muted,false,'right',numberObj);
 if(sub)text(s,sub,66,130,1148,62,26,C.muted);
 if(foot)text(s,foot,66,footY,1090,43,20,C.muted);
 coverage.push({slide:i,title,sourceSlide:seq[i-1],reportSections:[],sourceIds:[]});return s;
}
function note(s,body,ids,sections){
 const row=coverage.at(-1);row.sourceIds=[...new Set(ids)];row.reportSections=sections;
 const cites=row.sourceIds.map(id=>{const r=refMap[id];if(!r)throw new Error(id);return `${r.title}\n${r.date_label}\n${r.locator}\n${r.url}`;}).join('\n\n');
 s.speakerNotes.textFrame.setText(body+(cites?'\n\n参考资料\n'+cites:''));row.script=body;
}
function table(s,values,{x=64,y=200,w=1152,h=365,widths=null,fontSize=27,pad=10,existing=null}={}){
 let t=existing;
 if(t){t.setValues(values);t.frame={left:x,top:y,width:w,height:h};t.columnWidths=widths??Array(values[0].length).fill(w/values[0].length);}
 else t=s.tables.add({rows:values.length,columns:values[0].length,left:x,top:y,width:w,height:h,columnWidths:widths??Array(values[0].length).fill(w/values[0].length),values});
 t.styleOptions={headerRow:true,bandedRows:false};
 const rows=values.length,cols=values[0].length;
 t.cells.block({row:0,column:0,rowCount:rows,columnCount:cols}).assign({fill:C.white,textStyle:{typeface:font,fontSize,color:C.ink,lineSpacing:1.05},margins:{left:14,right:14,top:pad,bottom:pad},anchor:'center'});
 t.borders.assign({style:'solid',fill:C.gray,color:C.gray,width:.6});
 t.cells.block({row:0,column:0,rowCount:1,columnCount:cols}).assign({fill:C.navy,textStyle:{typeface:font,fontSize,bold:true,color:C.white}});
 for(let r=0;r<rows;r++)t.rows[r].height=h/rows;
 tableOwners.push(coverage.length);return t;
}
function steps(s,items,{x=66,y=205,w=760,gap=120,size=30}={}){
 items.forEach((a,k)=>{text(s,String(k+1).padStart(2,'0'),x,y+k*gap,55,45,28,C.teal,true);text(s,a[0],x+78,y+k*gap,w-78,45,size,C.navy,true);text(s,a[1],x+78,y+k*gap+49,w-78,66,27);});
}
// 1 Cover uses the original title layout.
{
 const s=ordered[0];for(const t of [...s.shapes.items]){
  if(t.frame.top===350)t.text='应用实践、技术流程与项目建议';
 }
 coverage.push({slide:1,title:'基金公司LLM应用调研',sourceSlide:1,sourceIds:[],reportSections:[]});
 note(s,'当前，内地基金公司已将大语言模型用于投研分析、数据查询、知识问答和合规审核，并在量化研究中开展文本因子提取、研究方案生成和工具调用。\n\n本次介绍围绕这四个方向展开，重点说明LLM在业务中承担什么工作、产生什么结果，以及这些经验如何用于本地部署与量化应用开发。',['FUND-007','FUND-300','FUND-200','FUND-308'],['摘要']);
}
// 2 Overview
{
 const s=page(2,'基金公司的四类LLM应用',{sub:'2026年二季度末非货公募规模前20家公司，另列大成补充案例',keepTable:true});
 table(s,[['应用方向','代表案例','LLM承担的工作'],['投研分析','富国、天弘、MENTOR','归纳资料，组织分析，形成观点与预测'],['数据查询','南方、易方达Index-Hub','识别需求，生成查询，解释返回结果'],['知识与合规','鹏华、汇添富','整理知识，提取风险信息，生成审核意见'],['LLM辅助量化','国内文本案例\nQuantaAlpha、Man','提取信号，提出研究方案，调用工具并迭代']],{y:218,h:365,widths:[205,365,582],fontSize:26,existing:s.tables.items[0]});
 text(s,'LLM已进入实际业务流程，本项目应推进本地部署与应用开发。',66,611,1110,48,29,C.teal,true);
 note(s,'调研以2026年二季度末非货公募规模前20家公司为主要样本，规模剔除ETF联接基金。样本约为3,448亿元至1.70万亿元，完整公司信息保留在附录。\n\n已披露的应用分布在多个业务环节。富国基金生成研报小结和市场观点，天弘基金开展财务归因，南方基金生成SQL并处理业务查询。鹏华基金和汇添富基金将模型接入知识与合规流程，量化研究则进一步使用模型提取文本信号、生成并迭代研究方案。\n\n这些案例提供了明确的应用方向。本项目应推进本地部署，将模型服务与数据和研究工具连接起来。',['FUND-400','FUND-007','FUND-300','FUND-200','FUND-308','FUND-220','FUND-352','EXT-QA'],['1 行业概览','摘要']);
}
// 3 Fullgoal
{
 const s=page(3,'富国基金：研报整理与市场观点生成',{foot:'富国基金报告的整体流程效果。研究系统包含约30万份研报。'});
 steps(s,[['筛选研究材料','按投资标的的相关性评分，选出研报'],['LLM归纳内容','形成知识小结，按指定研究方向分析'],['LLM生成观点','综合各份小结，形成市场观点']],{w:725,y:202,gap:123});
 text(s,'一周以上',891,214,310,80,49,C.navy,true);
 text(s,'原流程耗时',893,300,298,47,25,C.muted);
 text(s,'3小时以内',890,405,320,84,49,C.teal,true);
 text(s,'系统上线后',893,489,298,47,25,C.muted);
 note(s,'富国基金的市场观点流程使用本地LLM、提示词和研究数据服务。研究员指定投资标的与分析方向后，流程先对研报与标的的相关程度评分，筛选符合阈值的材料。LLM首先形成研报知识小结，之后按指定方向归纳，再综合小结生成市场观点。\n\n例如分析行业需求时，模型提炼各报告对需求变化的判断，形成分项小结和综合观点。富国基金也通过RAG提供知识问答，检索研报、行情和内部点评的相关片段，由模型生成答案并标记来源。\n\n公司报告，研究系统包含约30万份研报，相关流程上线后，原来一周以上的工作可缩短至3小时以内。该案例展示了本地LLM减少重复整理工作、支持研究观点生成的实际用途。',['FUND-007'],['2.1 富国基金']);
}
// 4 Tianhong
{
 const s=page(4,'天弘基金：LLM组织财务归因分析',{sub:'研究员提出盈利分析要求，FinAgent结合财报与工具数据形成解释'});
 table(s,[['分析层次','模型组织的内容'],['研究问题','企业净利润增长由哪些因素驱动'],['核心维度','收入、成本、费用'],['进一步分析','销量、单价、原材料、渠道'],['分析产物','结构化归因框架与解释文本']],{y:211,h:324,widths:[266,886],fontSize:28});
 text(s,'数日的整理与计算缩短至分钟级',66,574,1120,53,37,C.teal,true);
 note(s,'天弘基金的FinAgent将LLM、金融工具和业务智能体连接。系统接收复杂研究任务后，先拆解子任务，再调用金融数据接口或计算工具，最后综合结果。LLM负责理解研究要求、组织分析步骤和形成解释。\n\n盈利归因案例中，FinAgent把净利润问题展开为收入、成本和费用，再进一步分析销量、单价、原材料与渠道。模型将这些信息组织为结构化归因框架和解释文本，支持增长质量与持续性的判断。\n\n据天弘基金介绍，这一过程将原先需要数日的手工整理与计算缩短至分钟级，使研究员更快进入盈利驱动因素的分析。',['FUND-300'],['2.2 天弘基金']);
}
// 5 MENTOR
{
 const s=page(5,'MENTOR：预测结果进入下一轮判断',{sub:'易方达基金与高校研究人员于2025年共同发表的研究'});
 table(s,[['LLM任务','输入内容','模型输出'],['事件预测','上周热点与改进指导','下一周按市场影响排序的10条事件'],['行业排序','事件、历史表现与排序策略','行业名称的有序列表'],['反馈修订','先前预测与实际结果','下一轮使用的改进意见与策略文本']],{y:222,h:313,widths:[216,422,514],fontSize:28});
 text(s,'每轮结果形成新的策略文本，持续用于后续预测。',66,576,1120,61,31,C.teal,true);
 note(s,'MENTOR围绕事件预测和行业排序建立多次LLM调用流程。模型先生成预测，再根据实际结果形成反馈，并将改进意见用于后续预测。各次调用通过文本与列表交换信息。\n\n事件预测读取上周热点和改进指导，生成下一周按市场影响排序的10条事件。行业排序读取事件、历史表现和策略，返回行业名称的有序列表。周期结束后，反馈调用比较预测与实际结果，生成新的指导文字。该机制更新提示词中的策略文本，模型权重保持不变。\n\n论文实验中，MENTOR在美股与A股的行业排序相关性均超过所列动量和SEP基线。这个方法把预测、评价和修订连接起来，让每轮结果成为下一轮判断的输入。实验数据见附录。',['FUND-113','FUND-114'],['2.3 MENTOR']);
}
// 6 Southern
{
 const s=page(6,'南方基金：LLM将业务需求转成查询',{sub:'“小喃同学”整合5个以上系统与20个以上流程',keepTable:true});
 table(s,[['环节','LLM生成的内容','系统如何使用'],['理解需求','意图、参数与工作流','调度引擎安排执行节点'],['选择数据','相关数据表与字段范围','提供数据库结构和查询模板'],['生成查询','筛选、关联与分组SQL','数据库执行并返回结果'],['组织答复','面向业务问题的解释','结合统计与图表展示结果']],{y:211,h:345,widths:[191,439,522],fontSize:27,existing:s.tables.items[0]});
 text(s,'日均操作耗时下降约40%',66,593,1110,51,37,C.teal,true);
 note(s,'南方基金使用微调大模型识别业务意图、解析参数并编排工作流，再由调度引擎调用API、SQL、知识检索或Python解释器。\n\nSQL流程中，表格选择智能体读取问题和元数据，选出相关表。SQL撰写智能体根据表结构和模板生成语句，数据库执行后，回复智能体结合结果和原问题生成答复。例如按行业汇总指定评级和期限债券余额，模型需要识别统计日、评级、期限与分组要求，再形成相应查询。\n\n南方基金报告，整合5个以上系统和20个以上流程后，日均操作耗时下降约40%。LLM把需求理解、工具调用和结果解释连接起来，减少了跨系统切换与重复操作。',['FUND-200'],['3.1 南方基金']);
}
// 7 Index-Hub
{
 const s=page(7,'易方达Index-Hub：自然语言调用数据接口',{sub:'示例需求：查询沪深300前十大成分股'});
 steps(s,[['识别查询对象','指数为沪深300，代码为000300'],['选择接口与参数','依据接口目录选择成分股查询能力'],['形成数据答复','取得成分股及权重，说明对应的数据日期']],{w:1110,y:215,gap:125});
 text(s,'公开客户端提供接口目录、鉴权与缓存，LLM负责理解和组织查询。',66,614,1120,53,26,C.teal);
 note(s,'Index-Hub通过预定义接口提供指数查询能力。模型先识别查询对象，再根据目录选择功能和参数，通过客户端取得数据，最后组织比较与解释。\n\n以查询沪深300前十大成分股为例，模型识别指数和代码000300，选择成分股接口，取得成分股及权重后形成带日期的说明。这个基于公开任务说明的例子展示了接口目录如何把数据能力提供给模型。\n\n南方基金的方案根据数据表结构生成SQL，Index-Hub通过固定接口提供查询。两者都把LLM接入既有数据服务。本项目可以把已有数据库和研究接口整理成模型能够理解的工具目录。',['FUND-115','FUND-116','FUND-200'],['3.2 Index-Hub']);
}
// 8 Knowledge
{
 const s=page(8,'鹏华基金：资料形成知识答案与资讯摘要',{keepTable:true});
 table(s,[['','知识问答','投研资讯整理'],['提供给模型','问题与检索到的资料片段','公告、新闻、研报与标签要求'],['LLM的工作','理解上下文并组织回答','提取信息、生成标签并归纳内容'],['直接产物','基于资料的知识答案','资讯标签、个股要点与摘要']],{y:196,h:333,widths:[197,460,495],fontSize:28,existing:s.tables.items[0]});
 text(s,'围绕问题组织答案，围绕公司或事件整理资讯。',66,579,1120,70,33,C.teal,true);
 note(s,'鹏华基金通过RAG把内部知识资料提供给LLM。知识系统先解析、清洗和切分文档，并生成向量入库。使用者提出问题后，检索组件选取相关片段，连同原问题交给LLM，模型理解上下文并生成答案。\n\n投研资讯助手则读取公告、新闻和券商研报，提取信息并生成可定制标签，再整理个股舆情要点与摘要。标签支持筛选，摘要支持快速阅读。\n\n两类应用使用相近的模型能力，知识问答围绕问题组织答案，资讯整理围绕公司或事件组织信息，共同减少逐篇浏览和归纳材料的工作。',['FUND-308'],['4.1 鹏华基金']);
}
// 9 Compliance applications
{
 const s=page(9,'LLM进入材料审核与风险信息处理',{sub:'鹏华基金的营销审核与汇添富基金的风控应用'});
 table(s,[['公司','LLM处理什么','形成什么产物'],['鹏华基金','结合7类71项规则理解待审文案','风险疑点与修改建议'],['汇添富基金','读取托管风险邮件和风控条款','风险信息、条款答复与拦截依据']],{y:211,h:249,widths:[228,469,455],fontSize:28});
 text(s,'989条',68,508,350,65,49,C.teal,true);text(s,'有效修改建议',69,580,350,46,27);
 text(s,'91%',660,508,350,65,49,C.teal,true);text(s,'最新建议采纳率',661,580,410,46,27);
 text(s,'上述成果由鹏华基金报告',66,650,1100,33,20,C.muted);
 note(s,'鹏华基金的营销审核系统结合7类、71项规则检查风险提示、基金信息、业绩宣传和禁止性表达。LLM理解文案、识别疑点并提出修改意见，合规人员据此完成复核和发布审批。公司报告累计审核1,266篇文件，执行近6万项信息审核，产生989条有效修改建议，最新采纳率91%。\n\n汇添富基金使用LLM提取托管行风控邮件信息，并结合风控规则与法规、内控或合同原文的对应关系解释拦截依据。既有风控引擎执行规则计算，LLM补充材料理解和条款解释能力。\n\n这些应用把大量文本阅读与初步意见整理交给模型，使人工处理集中于规则适用和最终决定。',['FUND-308','FUND-220'],['4.2 鹏华与汇添富基金']);
}
// 10 Quant paths
{
 const s=page(10,'LLM辅助量化的两条路径');
 text(s,'文本信息形成研究信号',66,191,1100,57,39,C.teal,true);
 text(s,'公告、研报、新闻与舆情进入模型，\n形成事件记录和文本因子。',66,269,1135,99,31);
 text(s,'研究方案通过工具自动执行',66,426,1100,57,39,C.teal,true);
 text(s,'LLM提出假设和因子定义，调用代码与回测工具，\n再根据结果筛选和迭代。',66,504,1135,99,31);
 note(s,'LLM辅助量化主要沿两条路径展开。第一条从公告、研报、新闻和舆情中提取信息，把非结构化文本转为事件与因子。第二条由模型生成研究方案，通过数据、代码和回测工具执行，再依据结果筛选与迭代。\n\n富国基金已使用LLM提取政策敏感度因子，并根据因子绩效数据形成评价意见。广发基金介绍了从非结构化数据挖掘另类因子，华泰柏瑞基金将公告、纪要和舆情结构化后与量化信号结合。\n\n文本理解是国内基金引入LLM的重要入口。开源框架QuantaAlpha和Man的AlphaTrend进一步展示了研究方案生成与执行的组织方式。',['FUND-007','FUND-251','FUND-359','EXT-QA','FUND-323'],['5 LLM辅助量化','5.1 文本信号']);
}
// 11 Event extraction
{
 const s=page(11,'公告文本形成结构化事件记录',{sub:'说明性例子：拟将年产能由10万吨提高至15万吨，预计两年后投产，尚待审批',keepTable:true});
 table(s,[['LLM提取的字段','输出示意'],['事件与状态','扩产，计划，待审批'],['数量与单位','原产能10万吨，计划产能15万吨'],['投产安排','预计两年后投产'],['原文依据','保留对应公告原句']],{y:219,h:324,widths:[312,840],fontSize:28,existing:s.tables.items[0]});
 text(s,'LLM保留事件含义，结构化记录接入研究数据集。',66,585,1120,53,31,C.teal,true);
 note(s,'以扩产公告为例，LLM识别事件、数量、单位和投产安排，并保留“计划”“待审批”等决定事件含义的状态。模型的产物是统一字段的事件记录。\n\n系统随后可以计算50%的计划增幅，匹配证券、去重并记录首次可得时间，将事件接入研究数据集。量化团队在这些记录上定义事件变量、构造因子并开展回测。\n\n这一方法把分散在文本中的经营信息变成能够跨公司、跨时期比较的数据，利用模型的语言理解能力扩展研究材料。该公告是解释输出形式的示例。',['FUND-007','FUND-251','FUND-359'],['5.1 文本信号']);
}
// 12 QuantaAlpha tasks
{
 const s=page(12,'QuantaAlpha：LLM组织因子生成与迭代',{sub:'2026年开源研究框架，将多次模型调用连接到计算与回测工具',keepTable:true});
 table(s,[['模型任务','接收的材料','直接输出'],['规划方向','研究主题与差异要求','候选研究方向'],['构造因子','假设、字段与算子说明','因子定义、公式与表达式'],['核对和修正','假设、表达式与错误反馈','一致性意见与修正方案'],['解释与迭代','回测结果及研究记录','结果分析、新假设与修改方向']],{y:211,h:363,widths:[230,432,490],fontSize:27,existing:s.tables.items[0]});
 text(s,'模型把研究设想转为可执行方案，再把检验结果转为新的研究任务。',66,610,1120,49,28,C.teal,true);
 note(s,'QuantaAlpha把LLM接入研究方向规划、因子构造、语义核对和反馈迭代。规划调用接收初始方向与数量要求，返回包含directions数组的JSON，框架据此建立研究分支。\n\n随后，模型根据市场观察、金融知识和既有记录提出假设，再转换为因子说明、数学定义和符号表达式。表达式进入代码实现和历史数据计算。实现失败时，模型读取错误信息并提出修正。\n\n一致性调用同时读取假设、说明、公式和表达式，返回is_consistent、severity、overall_feedback与corrected_expression等字段。模型提供语义判断，程序组织检验与重试。最后，模型根据回测结果分析下一步需要改变什么，生成新的假设或融合方案。',['EXT-QA','EXT-QC'],['5.2 QuantaAlpha']);
}
// 13 Iteration example
{
 const s=page(13,'QuantaAlpha：回测反馈改变下一轮方案',{sub:'原论文附录C的一次因子交叉研究',keepTable:true});
 table(s,[['研究过程','具体内容'],['生成假设与因子','组合两类动量，生成价量表达式'],['取得回测反馈','Rank IC提高，信息比率略降，最大回撤扩大'],['LLM形成判断','暂不采用当前方案，补入波动状态后重新检验']],{y:213,h:302,widths:[288,864],fontSize:29,existing:s.tables.items[0]});
 text(s,'LLM综合回测反馈，提出下一轮的具体修改。',66,567,1120,61,33,C.teal,true);
 note(s,'这条记录希望组合持续动量与脆弱动量，并按市场波动状态调整权重。生成的子因子使用20日价格与成交量变动的相关性，乘以5日日内收益均值，再进行横截面排名。\n\n回测显示，子因子的Rank IC为0.0311，高于父记录的0.0216与0.0246。但相对于案例基准，信息比率由0.973降至0.963，超额收益最大回撤由约7.30%扩大至11.37%。模型综合结果，提出暂不采用并补充波动状态。\n\nLLM在这里将检验反馈转化为新的研究任务。表达式尚未完整体现假设中的状态调整机制，后续研究需要收紧经济解释与计算之间的对应关系。该次修改的后续结果未在论文中报告，案例与总体实验分别理解。',['EXT-QA','EXT-QC'],['5.3 研究实例']);
}
// 14 Man workflow, keep source image unchanged.
{
 const s=page(14,'Man AlphaTrend：批量实施并筛选研究方案',{keepImage:true,foot:'原始流程图来源：Man AHL，2026年2月11日。'});
 const im=s.images.items[0];im.frame={left:35,top:164,width:752,height:470};
 text(s,'研究员给出命题',830,192,380,48,31,C.teal,true);
 text(s,'LLM生成候选信号\n和参数变体',830,246,380,86,29);
 text(s,'工具完成实施与回测',830,360,380,88,31,C.navy,true);
 text(s,'LLM综合证据',830,485,380,48,31,C.teal,true);
 text(s,'解释差异，筛选方向，\n形成后续研究结论',830,537,380,86,29);
 note(s,'Man AHL的AlphaTrend专门面向趋势信号研究，把方案生成、实现、回测、分析和综合结论组织为预定义流程。LLM在不同节点处理明确任务，后续调用读取前面步骤的输出，多个独立调用能够并行探索同一命题的不同实现。\n\n研究员提供命题与约束后，模型生成候选信号和参数变体，进入代码实现与回测。取得结果后，模型结合基准、相关性和其他分析，解释方案差异并判断后续研究价值。\n\n作者用已知有效、预期较差和开放性命题检验该流程。AlphaTrend识别出已知改进机会，给出负面判断，并指出不同时期的表现差异。其价值在于批量实施、筛选方向，帮助研究员排除无效尝试并确定重点。',['FUND-323'],['5.4 Man AlphaTrend']);
}
// 15 Research tool ecosystem
{
 const s=page(15,'研究工具与代码生成接入LLM流程',{keepTable:true});
 table(s,[['案例','提供给模型的研究能力','业务用途'],['博时BSBox','数据访问、研究工具、独立运行环境','组合使用常用研究能力'],['中欧基金','100余项研究Skills','数据获取、财务建模与报告写作'],['NLPCC 2026任务','新闻、行情与投资模拟服务','形成投资决策并接收回测结果'],['AlphaQT-Bench','量化任务、数据结构与输出要求','生成Python代码并接受统一评价']],{y:195,h:375,widths:[267,480,405],fontSize:26,existing:s.tables.items[0]});
 text(s,'工具提供可执行能力，LLM根据研究要求选择和组织使用。',66,610,1120,53,30,C.teal,true);
 note(s,'博时BSBox和中欧基金展示了向模型提供数据访问、研究工具与Skills的实践。博时介绍了分用户运行环境和审计，中欧介绍了用于数据获取、财务建模和报告写作的100余项Skills。共同思路是把常用研究能力整理为可重复调用的工具。\n\n易方达基金参与的NLPCC 2026投资Agent任务则提供公开研究基线。模型根据新闻、行情和任务约束形成投资决策，回测服务执行模拟并返回结果。\n\nAlphaQT-Bench把代码生成设为独立任务。模型读取要求并返回Python实现，测试程序运行代码，与专家实现比较，检查时序和计算结构。量化团队可以沿这一方式把模型代码生成接入已有研发流程。',['FUND-215','FUND-356','FUND-119','EXT-AB'],['5.5 研究工具调用与代码生成']);
}
// 16 Decoupling
{
 const s=page(16,'模型服务与研究框架分别建设',{keepTable:true});
 table(s,[['组成','承担的职责','接口内容'],['模型服务','本地或API推理','任务上下文、生成内容与工具指令'],['研究框架','编排任务并保存研究记录','假设、执行结果与反馈'],['研究工具','数据读取、代码执行和回测','数据、运行结果与研究指标']],{y:210,h:311,widths:[235,419,498],fontSize:29,existing:s.tables.items[0]});
 text(s,'固定任务和工具，比较本地与API模型的实际表现。',66,576,1120,60,33,C.teal,true);
 note(s,'QuantaAlpha通过独立的APIBackend调用LLM，计算与回测在另外的环境中执行。这种分工使框架围绕稳定的任务和工具接口组织研究，模型的部署位置能够单独配置。\n\n本项目应沿这一结构建设。模型服务负责推理，研究框架负责任务编排与记录，数据、代码和回测工具完成具体操作。首先固定金融文本与因子研究任务，比较不同模型完成任务的质量，再结合延迟、资源和数据要求决定本地部署与API的使用方式。\n\n模型选型与量化应用开发因此能够分别推进，并通过一致的输入输出接口衔接。',['EXT-QC'],['5.6 模型服务与研究框架']);
}
// 17 Governance design
{
 const s=page(17,'数据与模型管理进入系统设计',{sub:'个人信息保护法、数据安全法与AMAC大模型技术应用规范',keepTable:true});
 table(s,[['应用环节','管理要求','实施安排'],['资料与知识答复','授权、版本和引用','检索权限与原文依据'],['SQL与研究代码','访问范围和执行控制','最小权限、隔离运行与操作记录'],['审核与风险意见','规则适用和发布责任','有效规则、人工复核与发布决定'],['模型更新','用途、评测和变更','模型版本、验证结果与责任分工']],{y:192,h:371,widths:[253,392,507],fontSize:27,existing:s.tables.items[0]});
 text(s,'管理要求落实到资料输入、工具执行和结果使用的具体环节。',66,610,1120,52,29,C.teal,true);
 note(s,'LLM应用涉及资料输入、内容生成、工具执行和业务使用。本地部署需要把数据与模型管理落实到各个环节。个人信息保护法要求确定处理依据，数据安全法覆盖相应数据分类与保护。检索与工具执行应实际实施权限控制，答案和返回结果遵守同样的访问范围。\n\n模型管理覆盖用途、评测、权限、变更与结果使用。AMAC大模型技术应用规范提供行业参考，属于团体标准，具体采用依据按法律和机构制度确定。\n\n项目实施应由内部合规、MRM与IT明确适用制度和COD接入条件，安排部署、评测与审批。SR 26-2面向所述美国银行机构，定义不涵盖生成式和Agentic AI，在本项目中作为比较材料。',['REG-002','REG-014','REG-009','REG-010','REG-012','REG-007','REG-008'],['6 合规要求']);
}
// 18 Services and external responsibilities
{
 const s=page(18,'服务范围与外部处理职责',{sub:'生成式人工智能服务管理暂行办法与证券基金信息技术管理办法',keepTable:true});
 table(s,[['使用方式','对应的实施要求'],['内部研究工具','按内部数据处理和信息系统要求建设'],['客户问答或对外发布','确定公众服务、内容管理和发布义务'],['外部OCR、嵌入或模型API','梳理处理位置、数据类型、数量和供应商角色'],['系统开发与运维','明确机构控制、供应商职责与替换安排']],{y:192,h:378,widths:[410,742],fontSize:28,existing:s.tables.items[0]});
 text(s,'本地模型与外部服务分别配置，管理覆盖完整的数据处理流程。',66,607,1120,56,29,C.teal,true);
 note(s,'生成式人工智能服务管理暂行办法第2条以向境内公众提供服务为适用条件，并排除未向公众提供此类服务的组织研发和应用。本项目以内部研究工具为起点，扩展到客户问答或对外发布时，重新确定公众服务与内容责任。\n\n外部OCR、嵌入服务、模型API、日志和远程运维都需要纳入流程梳理。按实际处理位置、供应商角色、数据类型和数量判断委托处理与出境要求，在原型接入服务时完成确认。\n\n证券基金信息技术管理办法第43条要求保留机构自身责任和重要系统控制，限制外部独立实施重要系统运维和日常安全管理，证监会另有规定的除外。第44至45条涉及审查、相应报送、协议和替换安排。',['REG-001','REG-003','REG-004','REG-005','REG-006','REG-016'],['6 合规要求','附录B']);
}
// 19 Pilot recommendation
{
 const s=page(19,'本地部署的首个量化原型');
 text(s,'公告事件提取',66,187,1110,70,48,C.teal,true);
 text(s,'LLM整理事件、状态、数量与原文依据，\n结构化记录接入量化研究数据集。',66,287,1120,106,33);
 text(s,'随后扩展到因子表达式与代码生成',66,449,1110,56,35,C.navy,true);
 text(s,'调用现有计算和回测工具，依据结果修订研究假设。',66,529,1120,85,31);
 note(s,'同业案例已提供明确的应用方向和技术流程。本项目应推进本地部署，以金融文本处理验证模型，并重点开发LLM辅助量化应用。\n\n建议首先开发公告事件提取原型，由模型整理事件、状态、数量和原文依据，接入研究数据集。这项任务能够直接连接语言理解能力与量化团队的数据需求。\n\n在此基础上增加因子表达式和代码生成，通过现有计算与回测工具检验方案，形成能够根据结果修订假设的研究Agent。只读查询和资料问答可以复用相同的模型服务与工具接口。',[],['7 项目建议']);
}
// 20 Project implementation
{
 const s=page(20,'下一阶段交付：模型服务与可运行原型');
 text(s,'5至8个',67,191,485,89,59,C.teal,true);text(s,'开放模型比较',69,288,475,54,31);
 text(s,'1个',734,191,455,89,59,C.teal,true);text(s,'本地GPU模型原型',736,288,470,54,31);
 text(s,'比较准确率、延迟、资源占用与人工修订时间',67,414,1120,61,32,C.navy,true);
 text(s,'交付工具接口与评测记录，为三年TCO分析提供依据。',67,517,1120,87,31);
 note(s,'按项目计划，下一阶段比较5至8个开放模型，并在本地GPU上部署一个模型完成金融文本任务。通过统一接口提供相同输入与工具，比较本地与API模型的准确率、延迟、资源占用和人工修订时间。\n\n阶段交付包括模型比较结果、可运行的本地原型、工具接口设计与评测记录。后续三年TCO分析据此核算设备、API、接入、运维与人工成本。\n\n以具体任务推进实施，将本次行业调研转化为量化部门可使用的研究能力。',[],['7 项目建议','PROJECT_PLAN Phase 2–3']);
}
// 21–23 Company appendix, all 21 report entries retained.
const cohort=JSON.parse(await fs.readFile(path.join(reportDir,'data/cohort.json'),'utf8'));
const companyRows=[
 ['易方达','指数查询与联合研究','接口参数、数据答复\n事件清单与行业排序','Index-Hub查询客户端\n高校联合MENTOR研究',['FUND-004','FUND-115','FUND-113']],
 ['华夏','大模型安全网关','2025年采购结果','北京世纪东凌中标',['FUND-001']],
 ['广发','理财问答与文本因子','理财答复\n另类因子研究','DeepSeek、Qwen\n2026年媒体调研',['FUND-009','FUND-251']],
 ['富国','研报归纳与因子评价','市场观点、知识答案\n政策因子与评价意见','本地LLM与RAG\nRay、ClickHouse',['FUND-007']],
 ['南方','需求解析与查询编排','工作流、SQL\n业务答复','智能体、API、Python\n系统权限控制',['FUND-200']],
 ['汇添富','风险邮件与条款问答','风险信息、条款答复\n拦截依据','DeepSeek-R1、QianWen\n与规则平台配合',['FUND-220']],
 ['景顺长城','文档处理与资料检索','文档与知识应用','本地模型、文字识别\n向量与检索重排',['FUND-251']],
 ['嘉实','ESG数据与研究','ESG数据支持','可持续投资报告\nLLM与其他AI未细分',['FUND-304']],
 ['博时','BSBox研究工具调用','可复用任务与工具结果','内部模型、独立环境\n研究协作与审计',['FUND-215']],
 ['鹏华','知识整理与材料审核','标签、摘要、知识答案\n修改建议','私有模型、RAG\n7类71项审核规则',['FUND-308']],
 ['招商','个股分析与财报点评','分析和信息提取结果','多个业务工作流\n信息提取模型',['FUND-251']],
 ['国泰','组合平台资料查询','资料查询与知识答复','Atlas 910B、DeepSeek\n另有BERT文本模块',['FUND-403']],
 ['永赢','安全GPT反钓鱼','邮件安全识别结果','2026年公司案例',['FUND-352']],
 ['工银瑞信','养老金运营\n历史FundGPT服务','运营平台与研究服务','历史合作：恒生聚源\n工银科技、智谱AI',['FUND-312','FUND-316']],
 ['天弘','研究任务与财务分析','归因框架与研究答复','FinAgent、Wind\n同花顺等工具',['FUND-300']],
 ['中欧','研究Skills协作','数据、建模与报告','100余项Skills\n2026年报道',['FUND-356','FUND-251']],
 ['华安','灵思资料与知识应用','资料处理与知识应用','2025年本地与API方案\nQwen、DeepSeek-R1',['FUND-150']],
 ['华泰柏瑞','文本与量化信号结合','结构化信息与研究支持','全链路投研系统\n自主回测Agent为展望',['FUND-359']],
 ['兴证全球','固收交易信息处理','交易文本提取结果','QTrade、iDeal\n具体LLM模块未明确',['FUND-011']],
 ['平安','AI青蚨资料整理','可追溯的研究内容','检索与可追溯输出\n2026年报道',['FUND-160']],
 ['大成','固收交易要素提取','供交易系统使用的要素','Qwen2.5与固收系统衔接',['FUND-013']]
];
for(let k=0;k<3;k++){
 const g=companyRows.slice(k*7,k*7+7);const s=page(21+k,`附录A  公司应用汇总（${k+1}/3）`,{foot:'规模单位：亿元。2026年二季度末非货公募规模，剔除ETF联接基金。大成为补充案例。',footY:665,keepTable:true});
 const v=[['公司','非货规模','主要任务','应用产物与进展','技术与合作信息'],...g.map(r=>{const a=cohort.find(x=>x.company===r[0]);return [r[0],a?a.aum_cny_100m.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2}):'补充案例',r[1],r[2],r[3]];})];
 table(s,v,{y:140,h:492,widths:[155,153,244,279,321],fontSize:23,pad:5,existing:s.tables.items[0]});
 note(s,g.map(r=>`${r[0]}：${r[1].replaceAll('\n','、')}。主要产物为${r[2].replaceAll('\n','、')}。技术与合作信息为${r[3].replaceAll('\n','、')}。`).join('\n\n')+'\n\n公司规模采用同一季度末非货公募口径，剔除ETF联接基金。历史采购、2025年案例与联合研究已分别注明。',['FUND-400',...g.flatMap(r=>r[4])],['附录A 表A']);
}
// 24 MENTOR results: original native table values retained.
{
 const s=page(24,'附录B  MENTOR行业排序结果',{sub:'2025年联合研究，文本样本覆盖2023至2024年',foot:'排序相关性采用Spearman系数，数字为原作者报告值。',keepTable:true});
 table(s,[['方法','美股11行业\nSpearman','A股9行业\nSpearman','A股前3\n命中率'],['动量基线','0.159','0.100','0.444'],['SEP + DeepSeek','0.078','0.118','0.472'],['MENTOR + DeepSeek','0.220','0.141','0.488'],['MENTOR + O1','0.221','0.173','0.439']],{y:214,h:337,widths:[425,245,245,237],fontSize:26,pad:7,existing:s.tables.items[0]});
 text(s,'MENTOR在两市场的行业排序相关性均超过表中基线。',66,590,1120,47,29,C.teal,true);
 note(s,'MENTOR的文本输入包括160,190篇中文KOL帖子与72,108篇英文财经新闻，样本覆盖2023至2024年。A股和美股行情分别来自Wind与Bloomberg，排序评价涉及9个和11个行业。\n\n表中MENTOR在两市场的行业排序相关性均超过基线。不同模型的目标存在取舍，A股O1版本的前3命中率低于DeepSeek版本与动量。复现需要取得版权数据、统一正文与补充材料的数据描述，并检查预训练数据与样本时段重合。',['FUND-113','FUND-114'],['附录C.1']);
}
// 25 QuantaAlpha results, preserve native chart and its workbook.
{
 const s=page(25,'附录C  QuantaAlpha的同模型对照',{sub:'均使用GPT-5.2，约150个因子交给相同LightGBM模型评价',foot:'沪深300测试期：2022年初至2025年12月26日。收益与回撤基于扣费后的超额收益。',keepTable:true,keepChart:true});
 const ch=s.charts.items[0];ch.frame={left:52,top:218,width:610,height:374};ch.yAxis={title:{text:'IC',textStyle:{typeface:font,fontSize:21,fill:C.muted}}};chartOwners.push(25);
 table(s,[['框架','年化\n超额收益','最大回撤'],['RD-Agent','3.58%','16.76%'],['AlphaAgent','1.11%','13.89%'],['QuantaAlpha','4.68%','11.80%']],{x:713,y:258,w:503,h:282,widths:[215,144,144],fontSize:23,pad:6,existing:s.tables.items[0]});
 note(s,'这里比较论文表1中使用同一GPT-5.2模型的三个框架，各方法产生约150个因子，再由相同LightGBM模型评价。QuantaAlpha的IC为0.0472，高于RD-Agent的0.0286与AlphaAgent的0.0347。\n\n训练期为2016至2020年，验证期2021年，测试期2022年初至2025年12月26日。组合每日选择50只等权股票，每次替换5只，采用次日开盘价，买入费率0.05%，卖出费率0.15%。\n\n使用DeepSeek-V3.2的消融实验中，移除修改环节后，IC从0.0461降至0.0382，年化超额收益从4.53%降至3.27%。完整对照中，其他传统或深度方法在部分组合指标上更好。作者报告主要运行约20小时、180万tokens，使用托管模型API和CPU回测。',['EXT-QA','EXT-QC'],['附录C.3']);
}
// 26 Man experiments, preserve native chart and its workbook.
{
 const s=page(26,'附录D  AlphaTrend的三类研究实验',{sub:'原作者用已知有效、预期较差和开放性命题检验研究流程',foot:'柱形表示原文所述约略集中或中心位置。作者历史模拟展示，基准经过有意简化。',keepChart:true});
 const ch=s.charts.items[0];ch.frame={left:64,top:210,width:820,height:390};ch.yAxis={title:{text:'Sharpe',textStyle:{typeface:font,fontSize:21,fill:C.muted}}};chartOwners.push(26);
 text(s,'恢复机制',926,254,286,44,31,C.teal,true);text(s,'识别已知改进机会',926,305,286,78,28);
 text(s,'开放探索',926,422,286,44,31,C.teal,true);text(s,'约0.70至1.00\n表现随时期变化',926,475,286,110,27);
 note(s,'作者从既有突破信号中移除了提高反应速度的机制，建立已知改进机会，再检验AlphaTrend的判断。恢复机制的方案Sharpe集中约1.05，简化基准约0.95。局部峰谷信号方案中心约0.80，几乎都低于基准。开放探索方案约为0.70至1.00，中心约0.85。\n\n这些实验说明研究流程能够识别改善、给出负面结果，并分析不同条件下的差异。原文图注截至2015年，部分正文涉及2012至2016年，资产池、成本与统计检验没有完整披露。\n\n在同一开放命题下，Claude 4.0 Sonnet方案的大部分两两相关性高于0.85，GPT-5约0.75至1.0，显示模型选择会影响候选方案的差异程度。',['FUND-323'],['附录C.2']);
}
// 27 AlphaQT code evaluation
{
 const s=page(27,'附录E  LLM生成量化代码的评价',{sub:'AlphaQT-Bench，270项任务与12个模型',keepTable:true});
 table(s,[['检查项目','评价内容'],['可执行性','能否运行并返回要求的结果'],['时间因果性','截断未来数据后，历史输出是否保持一致'],['功能正确性','结果是否符合任务定义与专家实现'],['计算结构','是否满足批量数组计算等约束']],{y:211,h:327,widths:[335,817],fontSize:28,existing:s.tables.items[0]});
 text(s,'四项同时通过的平均正确率',66,564,1120,41,27,C.muted);
 text(s,'93.7%  Gemini-2.5-Pro     81.9%  DeepSeek-V3',66,611,1120,48,30,C.teal,true);
 note(s,'AlphaQT-Bench包含270项任务并测试12个模型。LLM根据量化任务、数据结构和输出要求生成Python代码，程序分别检查运行、时序因果、功能和计算结构。\n\n四项同时通过的平均验证正确率，在论文模型样本中最高为93.7%，对应Gemini-2.5-Pro。开放权重模型中最高为81.9%，对应DeepSeek-V3。该指标评价代码对任务要求的实现质量。\n\n时间因果检查先用完整数据计算，再截断至较早时点重算，比较同一历史时点的输出。这类测试可以与量化团队现有代码评价结合，用统一标准筛选模型生成的实现。',['EXT-AB'],['5.5 代码生成','附录C.4']);
}

if(p.slides.items.length!==27||coverage.length!==27)throw new Error('Incorrect revision slide count');
await fs.mkdir(TMP,{recursive:true});await fs.mkdir(path.dirname(OUT),{recursive:true});await fs.mkdir(path.join(WS,'.codex-finalizer'),{recursive:true});
const stem=path.basename(OUT,'.pptx');const candidatePath=path.join(TMP,`${stem}.candidate.pptx`);
const reportSha=crypto.createHash('sha256').update(await fs.readFile(path.join(reportDir,'report.pdf'))).digest('hex');
const sourceSha=crypto.createHash('sha256').update(await fs.readFile(SOURCE)).digest('hex');
await fs.writeFile(path.join(WS,'src/slide-manifest.json'),JSON.stringify({reportCommit:'8801c3b',reportPdf:'reports/phase1-llm-industry-2026-09-09/report.pdf',reportPdfSha256:reportSha,sourceDeck:path.relative(REPO,SOURCE),sourceDeckSha256:sourceSha,researchCutoff:'2026-09-09',preparedDate:'2026-09-11',mainSlides:20,appendixSlides:7,slides:coverage},null,2)+'\n');
await (await PresentationFile.exportPptx(p)).save(candidatePath);
const renders=path.join(TMP,`draft-render-${stem}`);await fs.mkdir(renders,{recursive:true});
for(let i=0;i<p.slides.items.length;i++){
 const sl=p.slides.items[i];const b=await p.export({slide:sl,format:'png',scale:1});await fs.writeFile(path.join(renders,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await b.arrayBuffer()));
 const l=await sl.export({format:'layout'});await fs.writeFile(path.join(renders,`slide-${String(i+1).padStart(2,'0')}.layout.json`),await l.text());
}
const requirements={requiredNativeTableOwnerSlides:[...new Set(tableOwners)],requiredNativeChartOwnerSlides:[25,26],requiredEmbeddedWorkbookChartOwnerSlides:[25,26]};
execFileSync(PYTHON,[path.join(WS,'src/restore-chart-workbooks.py'),SOURCE,candidatePath],{stdio:'inherit'});
const result=await finalizePresentation({...requirements,workspaceDir:WS,candidatePath,finalPath:OUT,pythonExecutable:PYTHON,integrityValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit',...requirements.requiredNativeTableOwnerSlides.flatMap(n=>['--require-native-table-slide',String(n)])],materializeLiteralChartWorkbooks:false,fontPolicy:{basis:'reference',families:[font],referencePath:SOURCE,referenceSha256:sourceSha},verifyArtifactToolImport:true,receiptPath:path.join(WS,'.codex-finalizer',path.basename(OUT)+'.validation.json')});
console.log(JSON.stringify({output:OUT,slides:coverage.length,tableOwners,chartOwners,result},null,2));
const final=await PresentationFile.importPptx(await FileBlob.load(OUT));const finalRenders=path.join(TMP,`final-render-${stem}`);await fs.mkdir(finalRenders,{recursive:true});
for(let i=0;i<final.slides.items.length;i++){
 const b=await final.export({slide:final.slides.items[i],format:'png',scale:1});await fs.writeFile(path.join(finalRenders,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await b.arrayBuffer()));
}
console.log('Final package rendered.');
