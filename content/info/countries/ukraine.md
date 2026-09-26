---
title: Украина
weight: 1
bookToC: false
---

# Украина

Чемпионаты Украины проводятся с 1996 года. Статистика ещё в процессе сбора.

<style>
.country-tab-bar{display:flex;flex-wrap:wrap;gap:.25rem .15rem;margin:1.25rem 0 1rem;border-bottom:1px solid color-mix(in srgb,currentColor 35%,transparent)}
.country-tab-bar button{appearance:none;background:none;border:0;border-bottom:2px solid transparent;margin-bottom:-1px;padding:.45rem .85rem;cursor:pointer;font:inherit;color:inherit}
.country-tab-bar button.is-active{border-bottom-color:currentColor;font-weight:600}
.country-tab-hide-until-ready~*:not(.country-always-visible){display:none}
</style>
<script>
(function(){
function wrapTabs(){
  var starts=document.querySelectorAll(".country-tab-start");
  if(!starts.length)return;
  starts.forEach(function(start){
    var id=start.getAttribute("data-tab");
    var panel=document.createElement("div");
    panel.className="country-tab-panel";
    panel.id="country-tab-"+id;
    panel.setAttribute("role","tabpanel");
    var node=start.nextSibling;
    while(node){
      var next=node.nextSibling;
      if(node.nodeType===1&&node.classList&&node.classList.contains("country-tab-end")){
        node.remove();
        break;
      }
      if(node.nodeType===1&&node.classList&&node.classList.contains("country-tab-start"))break;
      panel.appendChild(node);
      node=next;
    }
    start.parentNode.insertBefore(panel,start);
    start.remove();
  });
  var hide=document.querySelector(".country-tab-hide-until-ready");
  if(hide)hide.remove();
  var buttons=document.querySelectorAll(".country-tab-bar [data-tab]");
  function show(id){
    document.querySelectorAll(".country-tab-panel").forEach(function(p){
      p.hidden=p.id!=="country-tab-"+id;
    });
    buttons.forEach(function(b){
      var on=b.getAttribute("data-tab")===id;
      b.classList.toggle("is-active",on);
      b.setAttribute("aria-selected",on?"true":"false");
    });
  }
  buttons.forEach(function(b){
    b.addEventListener("click",function(){show(b.getAttribute("data-tab"));});
  });
  function findTarget(hash){
    if(!hash)return null;
    function match(root){
      if(!root)return null;
      var el=root.getElementById?root.getElementById(hash):null;
      if(el)return el;
      if(root.querySelector){
        try{
          el=root.querySelector('[id="'+hash+'"], [name="'+hash+'"]');
          if(el)return el;
        }catch(e){}
      }
      var named=(root.getElementsByName?root.getElementsByName(hash):[]);
      if(named&&named.length)return named[0];
      return null;
    }
    var visible=document.querySelector(".country-tab-panel:not([hidden])");
    var el=match(visible)||match(document);
    if(el)return el;
    try{
      var decoded=decodeURIComponent(hash);
      if(decoded!==hash){
        hash=decoded;
        visible=document.querySelector(".country-tab-panel:not([hidden])");
        return match(visible)||match(document);
      }
    }catch(e){}
    return null;
  }
  function tabFromHash(){
    var hash=(location.hash||"").replace(/^#/,"");
    if(!hash)return buttons[0]&&buttons[0].getAttribute("data-tab");
    if(document.getElementById("country-tab-"+hash))return hash;
    var el=findTarget(hash);
    if(el){
      var panel=el.closest(".country-tab-panel");
      if(panel&&panel.id.indexOf("country-tab-")===0)return panel.id.slice("country-tab-".length);
    }
    return buttons[0]&&buttons[0].getAttribute("data-tab");
  }
  function reveal(){
    show(tabFromHash());
    var el=findTarget((location.hash||"").replace(/^#/,""));
    if(el)window.requestAnimationFrame(function(){el.scrollIntoView();});
  }
  reveal();
  window.addEventListener("hashchange",reveal);
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",wrapTabs);
else wrapTabs();
})();
</script>
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-chgk" aria-selected="false">Турниры по ЧГК</button><button type="button" role="tab" data-tab="game-ssi" aria-selected="false">Турниры по ССИ</button><button type="button" role="tab" data-tab="missing-data" aria-selected="false">Проблемы</button><button type="button" role="tab" data-tab="sources" aria-selected="false">Источники и благодарности</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th>Команда</th><th>Город</th><th>I</th><th>II</th><th>III</th><th>∑</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/540">Стирол</a></td>
<td>Горловка</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/28673">Команда Мороховского</a></td>
<td>Одесса</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/316">Мінус один («Минус один»)</a></td>
<td>Киев</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/29247">Порт Южный</a></td>
<td>Одесса</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/308">Номер 6</a></td>
<td>Донецк</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/210">От Винта - Братья по фазе</a></td>
<td>Харьков</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/27448">Keisecker</a></td>
<td>Киев</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/85771">seꏢes («senes»)</a></td>
<td>Киев</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/200">ОНУ им. Мечникова</a></td>
<td>Одесса</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/45704">От Винта</a></td>
<td>Харьков</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/26956">Приматы</a></td>
<td>Днепр</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/230">Команда Евгении Канищевой</a></td>
<td>Симферополь</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/27522">Смажені цвяхи</a></td>
<td>Киев</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="players"></div>

<a id="players"></a>

<table>
<thead>
<tr><th rowspan="2">Игрок</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">ЧГК</th><th colspan="3" style="text-align:center">ССИ</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/player/19990">Антон Мартыненко</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35124">Алексей Чирков</a></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27701">Антон Саввин</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23740">Владимир Островский</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30260">Евгений Спектор</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22935">Илья Новиков</a></td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19992">Андрей Мартыненко</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/66309">Александр Мудрый</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/49173">Александр Кондарев</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18053">Борис Левин</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26016">Владислав Пристинский</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17064">Игорь Кузьмин</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/49174">Илья Сименко</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21137">Кирилл Михайлов</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22331">Константин Науменко</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10946">Николай Жовнер</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9834">Ольга Дубинская</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18490">Дмитрий Литвинов</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19468">Виктория Маландина</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21952">Павел Муха</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7420">Эдуард Голуб</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8532">Евгений Гурт</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5195">Анатолий Вассерман</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/55074">Борис Бурда</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/79185">Владимир Шевчук</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21631">Ирина Морозовская</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/64681">Мария Докучаева</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/46459">Михаил Осадчий</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21632">Роман Морозовский</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/49162">Татьяна Богатырёва</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18809">Татьяна Луговская</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9094">Александр Демяненко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35077">Александр Чижов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33197">Алексей Филановский</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19533">Арсен Малиновский</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35877">Богдан Шевченко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10176">Виктория Евтушенко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9925">Владимир Дудчак</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12773">Владимир Итыгин</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/130038">Дмитрий Антоненко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30678">Дмитрий Стрильчук</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17034">Егор Кузьменко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/505">Иделия Айзятулова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7496">Катерина Коциевская</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/40201">Ксения Кучерова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/130019">Оксана Касянчук</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3278">Олег Беседин</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30030">Олег Соловьёв</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36398">Евгений Шляхов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/46788">Александр Мерзликин</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/80025">Александра Малыныч</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/44650">Алексей Востриков</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/58842">Андрей Темников</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32979">Виталий Фёдоров</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21176">Денис Михалёв</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5328">Дмитрий Великов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29516">Дмитрий Слободянюк</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13305">Евгения Канищева</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/128239">Елизавета Болотова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/109352">Никита Тищенко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7478">Павел Гольдин</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13304">Сергей Канищев</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/52202">Юлия Москалёва</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35563">Ян Шапиро</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29751">Ярослав Смолянинов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8850">Андрей Данченко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/155200">Игорь Цвяк</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5224">Тарас Вахрив</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-chgk"></div>

<a id="game-chgk"></a><a id="chgk_contents" name="chgk_contents"></a>

- [XXVII чемпионат Украины по спортивному ЧГК (2025, на украинском языке)](#chgk_2025)
- [XXVI чемпионат Украины по спортивному ЧГК (2022)](#chgk_2022)
- [XXV чемпионат Украины по спортивному ЧГК (2019)](#chgk_2019)
- [X чемпионат Украины по спортивному ЧГК (2004)](#chgk_2004)
- [IX чемпионат Украины по спортивному ЧГК (2002)](#chgk_2002)
- [VIII Открытый чемпионат Украины по спортивному ЧГК (2000)](#chgk_2000)
- [VI чемпионат Украины по спортивному ЧГК (1999)](#chgk_1999)
- [IV чемпионат Украины по спортивному ЧГК (1997)](#chgk_1997)
- [III чемпионат Украины по спортивному ЧГК (1996)](#chgk_1996)


**XXVII чемпионат Украины по спортивному «Что? Где? Когда?»** прошёл 27–28 сентября 2025 года в онлайне. Вопросы задавались на украинском языке. <a id="chgk_2025"></a>

Победитель: **[Мінус один («Минус один») (Киев)](https://rating.chgk.info/teams/316)**
- Владимир Островский
- Евгений Спектор
- Антон Саввин
- Александр Мудрый
- Кирилл Михайлов
- Владимир Шевчук

Второе место заняла команда [seꏢes («senes»)](https://rating.chgk.info/teams/85771) (Киев), третье — [«Смажені цвяхи»](https://rating.chgk.info/teams/27522) (Киев).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1Qcht6JL0mbzF7QyNT5BTcM_9alPasXWK3hIjn71grhM/edit?gid=583114730#gid=583114730). Больше информации о турнире — [в этом телеграм-канале](https://t.me/LigaUK/831) и [здесь](https://t.me/chgknews/1253).

*[К оглавлению](#chgk_contents)*

---

**XXVI чемпионат Украины по спортивному «Что? Где? Когда?»** прошёл 4–5 декабря 2021 года в Киеве. <a id="chgk_2022"></a>

Победитель: **[«Номер 6» (Донецк)](https://rating.chgk.info/teams/308)**
- Алексей Чирков
- Павел Муха
- Эдуард Голуб
- Виктория Маландина
- Мария Докучаева
- Михаил Осадчий

Второе место разделили команды [«Приматы»](https://rating.chgk.info/teams/26956) (Днепр) и [Мінус один («Минус один»)](https://rating.chgk.info/teams/316) (Киев). В сезоне 2021/2022 удалось провести только первый этап. Его результаты в августе 2022 года были признаны итогами всего чемпионата

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/13EiLBHZgttOm8rGm1xMGetezcV_x-v9z691KpjaAh3k/edit?gid=583114730#gid=583114730). Фотографии с турнира можно посмотреть по [этой ссылке](https://www.facebook.com/events/979057086285582?post_id=1017113002479990&view=permalink). Больше информации о турнире — [на сайте чемпионата](https://docs.google.com/spreadsheets/d/13EiLBHZgttOm8rGm1xMGetezcV_x-v9z691KpjaAh3k/edit?gid=1271955621#gid=1271955621), [в этом телеграм-канале](https://t.me/LigaUK/358), [в Facebook](https://www.facebook.com/events/979057086285582) и [здесь](https://t.me/chgknews/353).

*[К оглавлению](#chgk_contents)*

---

**XXV чемпионат Украины по спортивному «Что? Где? Когда?»** проходил в два этапа. Первый этап проходил 8–9 декабря 2018 года в Харькове, второй этап — 13–14 апреля 2019 года в Киеве. <a id="chgk_2019"></a>

Победитель: **[Мінус один («Минус один») (Киев)](https://rating.chgk.info/teams/316)**
- Владимир Островский
- Евгений Спектор
- Антон Саввин
- Александр Мудрый
- Ольга Дубинская
- Константин Науменко

Второе место заняла команда [Keisecker](https://rating.chgk.info/teams/27448) (Киев), третье — [«Номер 6»](https://rating.chgk.info/teams/308) (Донецк).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1AFoaaUcMyFaw0CmFsbYS1J042otAczLCpnxb099QeUo/edit?gid=1299839863#gid=1299839863).

Результаты первого этапа можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5344). Фотографии с турнира можно посмотреть по [этой ссылке](https://www.facebook.com/groups/1571471789754881/posts/2273463126222407/?__cft__[0]=AZgp9M64mZ5qY9p1h9MifY3zXwBAzqKJNi5shaPCYswSXCYmDiydI8aq4bM7hDS1BHN_xnwbq37yVamrNUmlJjObeKGA9wDPslLZYQnx410WnV0B4YFOhEQdn8NNEo7-kVc_u9L5RsigPG_M-QlF_3aXNZ56-l1iE3P6D4fyNL7hhKamAHv3iawGAQu7k90WqeymUHIkzdSoKxlI4TEtGidzlKBmK2xvzbY20oZnlQjXKX-6Kzc0DmtU6tDbkgwlobI&__tn__=%2CO%2CP-R). Больше информации о турнире — [в Facebook](https://www.facebook.com/events/1053568614816442/). Результаты второго этапа можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1iY4-xG9QSnLPVHob3PMUjuhu--nQBfadKMRsDdKgE1w/edit?fbclid=IwY2xjawUkeEdleHRuA2FlbQIxMQBwZG9mAWJyaWQRMU5Iam1yd1B1UjZSU05YQ2xzcnRjBmFwcF9pZBAyMjIwMzkxNzg4MjAwODkyAAEeeLBFDP5ac3s6k_ZMheKN5LlQlxmWoENHYKAR3I8z-ThGQSNDh2gj7VS3Ihw_aem_wHYVM8e1FIJR1X_IIYY0fQ&gid=970420865#gid=970420865). Больше информации о турнире — [на сайте чемпионата](https://docs.google.com/spreadsheets/d/1cjnLTWZhfBV1HgSmfF7vPF9feXSceO3OCYNScD1_tTg/edit?fbclid=IwY2xjawUkfIxleHRuA2FlbQIxMABwZG9mAWJyaWQRMU5Iam1yd1B1UjZSU05YQ2xzcnRjBmFwcF9pZBAyMjIwMzkxNzg4MjAwODkyAAEejA1wUFq8YX2oV_QjxAHq9dCFRnuh60rgaaT15xsy13-AWHfP1NVxC1KltI0_aem_w6b-UaHHBW38wJY8lsjURg&gid=614694312#gid=614694312), [в Facebook](https://www.facebook.com/events/351499475437794) и [здесь](https://www.facebook.com/LUCshchdkofficial/posts/pfbid034DHBXNTpEa3VnKxTEJoyPFVmTQWm8oCvpa9u5PSvy6dEi6FPkeYWuqExwJSTZdDhl?__cft__[0]=AZgPXLAChJMzKKNYXP1Wa4kfxushItsnN4K-SF47XVZDYHgALWVGOl9SXKVSMI60bqRQ3wvvf9c6gx_ndCTKmCGaHYKRq5bw8WXAaSetn21JK5NweWptDJRukZY69XNZLko9GYbraTUAVXFUrtEFeYYU_w&__tn__=%2CO%2CP-R).

*[К оглавлению](#chgk_contents)*

---

**X чемпионат Украины по спортивному «Что? Где? Когда?»** проходил в три этапа. Первый этап проходил 15 ноября 2003 года, второй этап — 17 января 2004 года, третий этап — 13 марта 2004 года в Симферополе. Результаты пока не учтены в статистике. <a id="chgk_2004"></a>

Полные результаты можно найти [на этой странице](http://letopis.chgk.info/200311Ukraine-res.html).

Результаты первого этапа можно найти [на этой странице](http://letopis.chgk.info/200311Ukraine-1scores.html). Результаты второго этапа можно найти [на этой странице](http://letopis.chgk.info/200311Ukraine-2scores.html). Результаты третьего этапа можно найти [на этой странице](http://letopis.chgk.info/200311Ukraine-3scores.html).

*[К оглавлению](#chgk_contents)*

---

**IX чемпионат Украины по спортивному «Что? Где? Когда?»** прошёл 18–19 октября 2002 года в Ровно. <a id="chgk_2002"></a>

Победитель: **[«От Винта - Братья по фазе» (Харьков)](https://rating.chgk.info/teams/210)**

*Состав команды [«От Винта - Братья по фазе»](https://rating.chgk.info/teams/210) (Харьков) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«ОНУ им. Мечникова»](https://rating.chgk.info/teams/200) (Одесса), третье — [«Команда Евгении Канищевой»](https://rating.chgk.info/teams/230) (Симферополь).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1316).

*[К оглавлению](#chgk_contents)*

---

**VIII Открытый чемпионат Украины по спортивному ЧГК** прошёл 5–7 октября 2000 года в Харькове. <a id="chgk_2000"></a>

Победитель: **[«Команда Мороховского» (Одесса)](https://rating.chgk.info/teams/28673)**
- Борис Бурда
- Татьяна Богатырёва
- Роман Морозовский
- Ирина Морозовская
- Татьяна Луговская
- Анатолий Вассерман

Второе место заняла команда [«Стирол»](https://rating.chgk.info/teams/540) (Горловка), третье — [«Порт Южный»](https://rating.chgk.info/teams/29247) (Одесса).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1044).

*[К оглавлению](#chgk_contents)*

---

**VI чемпионат Украины по спортивному «Что? Где? Когда?»** прошёл 9–11 сентября 1999 года в Виннице. <a id="chgk_1999"></a>

Победитель: **[«Стирол» (Горловка)](https://rating.chgk.info/teams/540)**
- Илья Сименко
- Александр Кондарев
- Владислав Пристинский
- Борис Левин
- Игорь Кузьмин
- Николай Жовнер

Второе место заняла [«Команда Мороховского»](https://rating.chgk.info/teams/28673) (Одесса), третье — [«Порт Южный»](https://rating.chgk.info/teams/29247) (Одесса).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1062).

*[К оглавлению](#chgk_contents)*

---

**IV чемпионат Украины по спортивному «Что? Где? Когда?»** прошёл 20 сентября 1997 года в Днепропетровске. <a id="chgk_1997"></a>

Победитель: **[«Стирол» (Горловка)](https://rating.chgk.info/teams/540)**

*Состав команды [«Стирол»](https://rating.chgk.info/teams/540) (Горловка) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«От Винта»](https://rating.chgk.info/teams/45704) (Харьков), третье — [«Команда Мороховского»](https://rating.chgk.info/teams/28673) (Одесса).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1576).

*[К оглавлению](#chgk_contents)*

---

**III чемпионат Украины по спортивному «Что? Где? Когда?»** прошёл 12–14 сентября 1996 года в Днепропетровске. <a id="chgk_1996"></a>

Победитель: **[«Стирол» (Горловка)](https://rating.chgk.info/teams/540)**

*Состав команды [«Стирол»](https://rating.chgk.info/teams/540) (Горловка) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла [«Команда Мороховского»](https://rating.chgk.info/teams/28673) (Одесса), третье — [«Порт Южный»](https://rating.chgk.info/teams/29247) (Одесса).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1552).

*[К оглавлению](#chgk_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ssi"></div>

<a id="game-ssi"></a><a id="ssi_contents" name="ssi_contents"></a>

- [XXIII чемпионат Украины по ССИ (2026, на украинском языке)](#ssi_2026)
- [XXII чемпионат Украины по ССИ (2025, на украинском языке)](#ssi_2025)
- [XXI чемпионат Украины по ССИ (2024, на украинском языке)](#ssi_2024)
- [XX чемпионат Украины по ССИ (2021)](#ssi_2021)
- [XIX чемпионат Украины по ССИ (2020)](#ssi_2020)


**XXIII чемпионат Украины по спортивной «Своей игре»** прошёл 7 мая–16 июня 2026 года в онлайне. Вопросы задавались на украинском языке. <a id="ssi_2026"></a>

Победитель: **[Антон Мартыненко](https://rating.chgk.info/player/19990)**

Второе место занял [Евгений Гурт](https://rating.chgk.info/player/8532), третье — [Андрей Данченко](https://rating.chgk.info/player/8850).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/10fwViAY_8ckXuNXn6GhzuQYt2KcSX1moNOMHepyNFg4/edit?gid=1028935314#gid=1028935314). Больше информации о турнире — [в этом телеграм-канале](https://t.me/c/2088760967/178) и [здесь](https://t.me/chgknews/1488).

Также доступно связанное с турниром видео: [финал чемпионата](https://www.youtube.com/watch?v=Q-_IrmnQNIM) (Youtube).

*[К оглавлению](#ssi_contents)*

---

**XXII чемпионат Украины по спортивной «Своей игре»** прошёл 28 апреля–8 июня 2025 года в онлайне. Вопросы задавались на украинском языке. <a id="ssi_2025"></a>

Победитель: **[Алексей Чирков](https://rating.chgk.info/player/35124)**

Второе место занял [Антон Мартыненко](https://rating.chgk.info/player/19990), третье — [Игорь Цвяк](https://rating.chgk.info/player/155200).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1cubdzIkVBgsRm--ZNEVYeSZDNLFAxFdua5gEmwfDd40/edit?gid=1915504037#gid=1915504037). Больше информации о турнире — [в этом телеграм-канале](https://t.me/LigaUK/772) и [здесь](https://t.me/chgknews/1166).

Также доступно связанное с турниром видео: [финал чемпионата](https://www.youtube.com/watch?v=GY8nu87C8o4) (Youtube).

*[К оглавлению](#ssi_contents)*

---

**XXI чемпионат Украины по спортивной «Своей игре»** прошёл 6 мая–15 июня 2024 года в онлайне. Вопросы задавались на украинском языке. <a id="ssi_2024"></a>

Победитель: **[Антон Мартыненко](https://rating.chgk.info/player/19990)**

Второе место занял [Андрей Мартыненко](https://rating.chgk.info/player/19992), третье — [Алексей Чирков](https://rating.chgk.info/player/35124).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1-0CTHL8G__Z89NyMnEoWKZCXCyCc_9Pt6eJakt23fD0/edit?gid=671782412#gid=671782412). Больше информации о турнире — [в этом телеграм-канале](https://t.me/vt_luk/34) и [здесь](https://t.me/chgknews/870).

*[К оглавлению](#ssi_contents)*

---

**XX чемпионат Украины по спортивной «Своей игре»** прошёл 4–5 декабря 2021 года в Киеве. <a id="ssi_2021"></a>

Победитель: **[Антон Мартыненко](https://rating.chgk.info/player/19990)**

Второе место занял [Илья Новиков](https://rating.chgk.info/player/22935), третье — [Андрей Мартыненко](https://rating.chgk.info/player/19992).

Фотографии с турнира можно посмотреть по [этой ссылке](https://www.facebook.com/photo/?fbid=1902130196640897&set=a.1902122199975030).

*[К оглавлению](#ssi_contents)*

---

**XIX чемпионат Украины по спортивной «Своей игре»** прошёл 13–14 октября 2019 года в Киеве. <a id="ssi_2020"></a>

Победитель: **[Дмитрий Литвинов](https://rating.chgk.info/player/18490)**

Второе место занял [Евгений Шляхов](https://rating.chgk.info/player/36398), третье — [Тарас Вахрив](https://rating.chgk.info/player/5224).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1jmOqeB3uclt4mc6wZ259Zn_eCFakcinBcMdFkRLQfPs/edit?fbclid=IwY2xjawUkcHhleHRuA2FlbQIxMABwZG9mAWJyaWQRMU5Iam1yd1B1UjZSU05YQ2xzcnRjBmFwcF9pZBAyMjIwMzkxNzg4MjAwODkyAAEeeYIZBkewccrIr9l_ZYTAo3WZQUm5MnuLDgzypNRl50DyjDatWj0Z4cx7u3w_aem_-ihH8iOYJULyE9ql5wEdag&gid=1045047531#gid=1045047531). Фотографии с турнира можно посмотреть по [этой ссылке](https://www.facebook.com/media/set?vanity=LUCshchdkofficial&set=a.1256451341208789). Больше информации о турнире — [в Facebook](https://www.facebook.com/events/673565669777449/).

*[К оглавлению](#ssi_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="missing-data"></div>

<a id="missing-data"></a>

Ниже собрана информация о том, каких данных не хватает в том или ином турнире.

<table>
<thead>
<tr><th>Год</th><th>Турнир</th><th>Чего не хватает</th></tr>
</thead>
<tbody>
<tr><td>2022</td><td>XXVI чемпионат Украины по ЧГК</td><td>неизвестны составы обладателей второго и третьего мест.</td></tr>
<tr><td>2004</td><td>X чемпионат Украины по ЧГК</td><td>неизвестно место проведения.</td></tr>
<tr><td>2004</td><td>X чемпионат Украины по ЧГК</td><td>неизвестно место проведения.</td></tr>
<tr><td>2004</td><td>X чемпионат Украины по ЧГК</td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2002</td><td><a href="https://rating.chgk.info/tournament/1316">IX чемпионат Украины по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго места.</td></tr>
<tr><td>2000</td><td><a href="https://rating.chgk.info/tournament/1044">VIII Открытый чемпионат Украины по спортивному ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>1999</td><td><a href="https://rating.chgk.info/tournament/1062">VI чемпионат Украины по ЧГК</a></td><td>неизвестны составы обладателей второго и третьего мест.</td></tr>
<tr><td>1997</td><td><a href="https://rating.chgk.info/tournament/1576">IV чемпионат Украины по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>1996</td><td><a href="https://rating.chgk.info/tournament/1552">III чемпионат Украины по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="sources"></div>

<a id="sources"></a>

Здесь указан список источников, откуда взята та или иная информация на этой странице.

<table>
<thead>
<tr><th>Турнир</th><th>Год</th><th>Источники</th></tr>
</thead>
<tbody>
<tr><td>XXVI чемпионат Украины по ЧГК</td><td>2021</td><td><a href="https://www.facebook.com/photo/?fbid=1902129776640939&amp;set=a.1902122199975030">фото в мероприятии чемпионата в Фейсбуке</a> (состав «Приматов»), <a href="https://www.facebook.com/photo/?fbid=1902128633307720&amp;set=a.1902122199975030">фото в мероприятии чемпионата в Фейсбуке</a> (Итыгин был в составе «Приматов»), <a href="https://www.facebook.com/photo/?fbid=1902129206640996&amp;set=a.1902122199975030">фото в мероприятии чемпионата в Фейсбуке</a> (Малиновский был в составе «Приматов»), <a href="https://www.facebook.com/photo/?fbid=1901389066715010&amp;set=a.1901397673380816">фото в мероприятии чемпионата в Фейсбуке</a> (состав «Минус один»), <a href="https://www.facebook.com/photo/?fbid=1902135033307080&amp;set=a.1902122199975030">фото в мероприятии чемпионата в Фейсбуке</a> (состав «Номер 6»)</td></tr>
<tr><td>XXV чемпионат Украины по ЧГК</td><td>2019</td><td><a href="https://www.facebook.com/groups/1571471789754881/posts/2336588419909877/?__cft__[0]=AZgVcQLnz-ExBun4cjFXYmQDbv4uM6uJbJT3qNCBZdc13nSQzdTc57-SIXD9ZYhbrDZ35_ZqAyKSnTx20kKIG7MrjlJHi4_7oB19luYefJj_I_BgV_4v586k0hAvqWNck-_94PKtQSISPL_IpRAyISRrYCQi5LvQTRauoErEUhSSK-Ryl8EUPvfiFb4l-A&amp;__tn__=%2CO%2CP-R">https://www.facebook.com/groups/1571471789754881/posts/2336588419909877/?__cft__[0]=AZgVcQLnz-ExBun4cjFXYmQDbv4uM6uJbJT3qNCBZdc13nSQzdTc57-SIXD9ZYhbrDZ35_ZqAyKSnTx20kKIG7MrjlJHi4_7oB19luYefJj_I_BgV_4v586k0hAvqWNck-_94PKtQSISPL_IpRAyISRrYCQi5LvQTRauoErEUhSSK-Ryl8EUPvfiFb4l-A&amp;__tn__=%2CO%2CP-R</a></td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
