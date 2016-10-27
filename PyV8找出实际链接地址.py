#-*- coding:utf-8-*-
import PyV8
import re
js='''<script type="text/javascript">function rS6(rS6_){function _r(rS6_){function pa(){return getName();}function rS6_(){}return pa();return rS6_}; return _r(rS6_);}_eODsD = window;function GXr(GXr_){function _G(GXr_){function re(){return getName();}function GXr_(){}return re();return GXr_}; return _G(GXr_);}function dr(dr_){function d(){return getName();};return d();return 'dr'}function fG1(){'fG1';function _f(){return '&e'}; return _f();}Ns=function(){'return Ns';return 't';};_Jq55l = 'replace';lP=function(){'lP';var _l=function(){return '.'}; return _l();};function tY(){'return tY';return '2'}function oUt(){'return oUt';return '=d'}function H0(){'H0';function _H(){return '='}; return _H();}function AW(){'return AW';return '/'}_vbkl7 = location;function o85(){'return o85';return '_d'}function c2(){'return c2';return '2'}KG=function(){'KG';var _K=function(){return '2'}; return _K();};function getName(){var caller=getName.caller;if(caller.name){return caller.name} var str=caller.toString().replace(/[\s]*/g,"");var name=str.match(/^function([^\(]+?)\(/);if(name && name[1]){return name[1];} else {return '';}}bww=function(bww_){var _b=function(bww_){'return bww';return bww_;}; return _b(bww_);};P7='g';N8=function(){'N8';var _N=function(){return '&'}; return _N();};vt='x';tWY=function(tWY_){'return tWY';return tWY_;};up=function(){'up';var _u=function(){return 'a'}; return _u();};I75=function(I75_){'return I75';return I75_;};X4=function(){'X4';var _X=function(){return '2'}; return _X();};function Ts(Ts_){function _T(Ts_){function p(){return getName();}function Ts_(){}return p();return Ts_}; return _T(Ts_);}function EG(EG_){function c(){return getName();};return c();return 'EG'}Sn=function(){'Sn';var _S=function(){return '='}; return _S();};fO=function(){'fO';var _f=function(){return 'f'}; return _f();};iz=function(){'iz';var _i=function(){return '9'}; return _i();};d1M=function(d1M_){'return d1M';return d1M_;};function z4(z4_){function h(){return getName();};return h();return 'z4'}qphj=function(){'return qphj';return 'tid';};function Gz(Gz_){function _G(Gz_){function a(){return getName();}function Gz_(){}return a();return Gz_}; return _G(Gz_);}_rEHkj = 'href';function UZ(UZ_){function u(){return getName();};return u();return 'UZ'}function vv(vv_){function _v(vv_){function e(){return getName();}function vv_(){}return e();return vv_}; return _v(vv_);}function TC(){'return TC';return '1'}_vSe9P = 'assign';function B9A(B9A_){function si(){return getName();};return si();return 'B9A'}lU='e';location[_Jq55l](AW()+fO()+I75('or')+UZ('E7')+(function(){'return F4';return 'm'})()+lP()+(function(KVL_){'return KVL';return KVL_})('ph')+Ts('gg')+bww('?m')+(function(vx3_){return (function(vx3_){return vx3_;})(vx3_);})('od')+H0()+tWY('vi')+vv('SR')+(function(){'return DM';return 'w'})()+Ns()+z4('wU')+GXr('O2U')+up()+dr('KU')+N8()+qphj()+(function(){'return T9H4';return (function(){return '=22';})();})()+c2()+tY()+(function(){'return yq';return (function(){return '1';})();})()+TC()+X4()+fG1()+vt+(function(p5x_){return (function(p5x_){return p5x_;})(p5x_);})('tr')+Gz('Pw')+Sn()+rS6('vpW')+P7+(function(){'return b33Z';return 'e%3'})()+(function(hV6_){'return hV6';return hV6_})('D1')+(function(F0F_){return (function(F0F_){return F0F_;})(F0F_);})('&p')+'ag'+lU+(function(){'return K0';return (function(){return '=';})();})()+(function(Wma_){return (function(Wma_){return Wma_;})(Wma_);})('1&')+o85()+B9A('VQK')+(function(CWj_){return (function(CWj_){return CWj_;})(CWj_);})('gn')+oUt()+d1M('a0')+(function(){'return fo';return (function(){return 'a';})();})()+EG('w5')+KG()+(function(){'return Em';return 'b'})()+iz());_eODsD.href=AW()+fO()+I75('or')+UZ('E7')+(function(){'return F4';return 'm'})()+lP()+(function(KVL_){'return KVL';return KVL_})('ph')+Ts('gg');</script>'''
#去掉<script>标签
js=js[31:-9]
for st in ['window','location',"'assign'","'href'","'replace'"]:
    equal=re.findall('[_A-Za-z0-9 =]+%s;'%st,js)#找到变量赋值等式
    if equal==[]:#有可能没有
        continue
    else:
        equal=equal[0]
    var=equal.split('=')[0].strip()#找出变量名
    #把等式干掉
    js=js.replace(equal,'')
    #把变量替换成它真正的意思
    js=js.replace(var,st)
    #把['xx'] 替换成 .xx
    js=js.replace("['%s']"%st.strip("'"),'.%s'%st.strip("'"))
#将 window.href= 后的内容踢掉，因为当PyV8只输出最后一个等式的值
if re.findall('window\.href=.+',js)!=[]:
    js=js.replace(re.findall('window\.href=.+',js)[0],'')
#删掉location.xxx=
js=js.replace('location.href=','').replace('location.replace','').replace('location.assign','')
#交给你了-v-
ctxt2 = PyV8.JSContext()
ctxt2.enter()
print ctxt2.eval(js)