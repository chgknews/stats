---
title: Азербайджан
weight: 1
bookToC: false
---

# Азербайджан

Чемпионаты Азербайджана по брейн-рингу проводятся с 2001 года, по спортивному ЧГК — с 2002 года. Ниже можно увидеть статистику по всем призёрам — как командам, так и игрокам. Также в отдельных вкладках можно найти информацию о чемпионатах страны по той или иной дисциплине.

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-chgk" aria-selected="false">Турниры по ЧГК</button><button type="button" role="tab" data-tab="game-brain" aria-selected="false">Турниры по БР</button><button type="button" role="tab" data-tab="missing-data" aria-selected="false">Проблемы</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th rowspan="2">Команда</th><th rowspan="2">Город</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">ЧГК</th><th colspan="3" style="text-align:center">БР</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/299">Команда Гусейнова</a></td>
<td>Баку</td>
<td>5</td>
<td>4</td>
<td>3</td>
<td>12</td>
<td>5</td>
<td>3</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/243">Команда Касумова</a></td>
<td>Баку</td>
<td>5</td>
<td>4</td>
<td>1</td>
<td>10</td>
<td>5</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/6074">Brainstorm</a></td>
<td>Баку</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/67979">Поминки по финикам</a></td>
<td>Баку</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/45599">Jazz</a></td>
<td>Баку</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/2723">Yo!J</a></td>
<td>Баку</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/242">Команда Азимова</a></td>
<td>Баку</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/40131">М4А1</a></td>
<td>Баку</td>
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
<td><a href="https://rating.chgk.info/teams/268">Команда Алиева</a></td>
<td>Баку</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/6075">Слон в удаве</a></td>
<td>Баку</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/5842">КиПЛ</a></td>
<td>Баку</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/32752">Команда Лятифова</a></td>
<td>Баку</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/487">Огуз</a></td>
<td>Баку</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/6521">Эверест</a></td>
<td>Баку</td>
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
<td><a href="https://rating.chgk.info/teams/2271">Команда Бабаева</a></td>
<td>Баку</td>
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
<td><a href="https://rating.chgk.info/teams/543">Команда Мусаева</a></td>
<td>Баку</td>
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
<td><a href="https://rating.chgk.info/teams/1611">ТН</a></td>
<td>Баку</td>
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
<td><a href="https://rating.chgk.info/teams/33236">Команда Зейналова</a></td>
<td>Баку</td>
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
<td><a href="https://rating.chgk.info/teams/32841">Команда Рагимова</a></td>
<td>Баку</td>
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
<div class="country-tab-start" data-tab="players"></div>

<a id="players"></a>

<table>
<thead>
<tr><th rowspan="2">Игрок</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">ЧГК</th><th colspan="3" style="text-align:center">БР</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/player/23537">Роман Оркодашвили</a></td>
<td>4</td>
<td>6</td>
<td>3</td>
<td>13</td>
<td>4</td>
<td>6</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22133">Рауф Наджафли (Наджафов)</a></td>
<td>5</td>
<td>4</td>
<td>2</td>
<td>11</td>
<td>5</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13721">Балаш Касумов</a></td>
<td>5</td>
<td>3</td>
<td>1</td>
<td>9</td>
<td>5</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/475">Джамиля Азизова</a></td>
<td>5</td>
<td>2</td>
<td>2</td>
<td>9</td>
<td>5</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8610">Фаик Гусейнов</a></td>
<td>5</td>
<td>2</td>
<td>2</td>
<td>9</td>
<td>5</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19170">Эмиль Мадатов</a></td>
<td>5</td>
<td>2</td>
<td>2</td>
<td>9</td>
<td>5</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21889">Азиз Муршудли</a></td>
<td>4</td>
<td>4</td>
<td>1</td>
<td>9</td>
<td>4</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/323">Заур Агаев</a></td>
<td>0</td>
<td>3</td>
<td>6</td>
<td>9</td>
<td>0</td>
<td>3</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/59">Руфат Абдулла</a></td>
<td>1</td>
<td>3</td>
<td>4</td>
<td>8</td>
<td>1</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1872">Аднан Ахундов</a></td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>7</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31184">Эльман Талыбов</a></td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>6</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8450">Анар Гулиев</a></td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>6</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27998">Джамиль Салманов</a></td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>6</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/476">Анар Азимов</a></td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>5</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17284">Ильхам Кумбатов</a></td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27879">Саид Садыхов</a></td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>5</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20522">Руфат Мейбализаде</a></td>
<td>0</td>
<td>2</td>
<td>3</td>
<td>5</td>
<td>0</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9265">Орхан Джафаров</a></td>
<td>0</td>
<td>1</td>
<td>4</td>
<td>5</td>
<td>0</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32579">Алексей Уланов</a></td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1871">Аббас Ахундов</a></td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8747">Акпер Дадашлы</a></td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/236">Дмитрий Авдеенко</a></td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1646">Ровшан Аскеров</a></td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/39945">Яна Лялякина</a></td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/47536">Эльнур Гасымзаде</a></td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32886">Джахангир Фараджуллаев</a></td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/59481">Расул Бабазаде</a></td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19101">Тимур Ляпин</a></td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36925">Фуад Эминов</a></td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/39926">Малик Рамазанзаде</a></td>
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
<td><a href="https://rating.chgk.info/player/7047">Илья Гинзбург</a></td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/856">Теймур Алиев</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6418">Хафиз Гайыб</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/78471">Эмин Расулзаде</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/72279">Денис Шабанов</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12033">Нигяр Ибрагимова</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/878">Фариз Аликишибеков</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/100822">Джамиль Ализаде</a></td>
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
<td><a href="https://rating.chgk.info/player/96417">Кянан Гурбатли</a></td>
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
<td><a href="https://rating.chgk.info/player/66638">Мурад Ахундов</a></td>
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
<td><a href="https://rating.chgk.info/player/22132">Анар Наджафли</a></td>
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
<td><a href="https://rating.chgk.info/player/39933">Борис Царицын</a></td>
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
<td><a href="https://rating.chgk.info/player/6816">Джейхун Гейбатов</a></td>
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
<td><a href="https://rating.chgk.info/player/19724">Кёнуль Мамедова</a></td>
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
<td><a href="https://rating.chgk.info/player/49160">Фуад Мусаев</a></td>
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
<td><a href="https://rating.chgk.info/player/1907">Гюнель Бабаева</a></td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21830">Мурад Мурадов</a></td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31140">Эргюн Тагиев</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8743">Вюгар Дадашев</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19715">Сеймур Мамедов</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/107872">Анна Гаузер</a></td>
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
<td><a href="https://rating.chgk.info/player/208597">Владимир Бабиор</a></td>
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
<td><a href="https://rating.chgk.info/player/112460">Гейдар Гамзаев</a></td>
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
<td><a href="https://rating.chgk.info/player/31949">Евгений Томашевский</a></td>
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
<td><a href="https://rating.chgk.info/player/11522">Елена Захарова</a></td>
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
<td><a href="https://rating.chgk.info/player/102108">Елизавета Ежергина</a></td>
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
<td><a href="https://rating.chgk.info/player/223827">Ильхам Гумбатов</a></td>
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
<td><a href="https://rating.chgk.info/player/122695">Илья Мурзинов</a></td>
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
<td><a href="https://rating.chgk.info/player/1833">Назлы Ахмедова</a></td>
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
<td><a href="https://rating.chgk.info/player/49158">Роман Аллояров</a></td>
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
<td><a href="https://rating.chgk.info/player/56294">Сеймур Агаев</a></td>
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
<td><a href="https://rating.chgk.info/player/8455">Теймур Гулиев</a></td>
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
<td><a href="https://rating.chgk.info/player/49159">Фариз Рзаев</a></td>
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
<td><a href="https://rating.chgk.info/player/223828">Хафиз Гаибов</a></td>
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
<td><a href="https://rating.chgk.info/player/21865">Шахин Мургузов</a></td>
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
<td><a href="https://rating.chgk.info/player/984">Эльнур Амикишиев</a></td>
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
<td><a href="https://rating.chgk.info/player/12731">Эмиль Исмаилов</a></td>
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
<td><a href="https://rating.chgk.info/player/8599">Абдулазим Гусейнов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10631">Илькин Етирмишли</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19153">Октай Магеррамов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Рустам Рустамов</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/441">Эльдар Адильзаде</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34875">Юрий Чернов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2054">Джавид Бадалбейли</a></td>
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
<td><a href="https://rating.chgk.info/player/52103">Джалал Оруджев</a></td>
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
<td><a href="https://rating.chgk.info/player/33672">Илькин Халилов</a></td>
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
<td><a href="https://rating.chgk.info/player/34480">Максим Цурков</a></td>
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
<td><a href="https://rating.chgk.info/player/19699">Мамедшакир Мамедзаде</a></td>
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
<td><a href="https://rating.chgk.info/player/2064">Ширин Баджанова</a></td>
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
<td><a href="https://rating.chgk.info/player/860">Эмин Алиев</a></td>
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
<td><a href="https://rating.chgk.info/player/20963">Лала Мирзоева</a></td>
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
<td><a href="https://rating.chgk.info/player/24364">Мурад Пашазаде</a></td>
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
<td><a href="https://rating.chgk.info/player/2362">Наиля Баннаева</a></td>
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
<td><a href="https://rating.chgk.info/player/7419">Ольга Голуб</a></td>
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
<td><a href="https://rating.chgk.info/player/8608">Султан Гусейнов</a></td>
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
<td><a href="https://rating.chgk.info/player/1906">Эмин Бабаев</a></td>
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
<td><a href="https://rating.chgk.info/player/6719">Айнур Гасанова</a></td>
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
<td><a href="https://rating.chgk.info/player/1711">Анар Атакишиев</a></td>
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
<td><a href="https://rating.chgk.info/player/19794">Анар Мансуров</a></td>
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
<td><a href="https://rating.chgk.info/player/9246">Вагиф Джамалов</a></td>
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
<td><a href="https://rating.chgk.info/player/19703">Джавид Мамедов</a></td>
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
<td><a href="https://rating.chgk.info/player/20959">Ибрагим Мирзоев</a></td>
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
<td><a href="https://rating.chgk.info/player/17658">Кямран Захид</a></td>
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
<td><a href="https://rating.chgk.info/player/36115">Олег Шибаев</a></td>
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
<td><a href="https://rating.chgk.info/player/47496">Пярвиз Мамедов</a></td>
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
<td><a href="https://rating.chgk.info/player/22265">Сагиф Намазов</a></td>
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
<td><a href="https://rating.chgk.info/player/21893">Таир Мусаев</a></td>
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
<td><a href="https://rating.chgk.info/player/39906">Теймур Бабаев</a></td>
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
<td><a href="https://rating.chgk.info/player/30851">Турал Султанов</a></td>
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
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-chgk"></div>

<a id="game-chgk"></a><a id="chgk_contents" name="chgk_contents"></a>

- [XVI чемпионат Азербайджана по спортивному ЧГК (2026)](#chgk_2026)
- [XV чемпионат Азербайджана по спортивному ЧГК (2025)](#chgk_2025)
- [XIV чемпионат Азербайджана по спортивному ЧГК (2024)](#chgk_2024)
- [XIII чемпионат Азербайджана по спортивному ЧГК (2023)](#chgk_2023)
- [XII чемпионат Азербайджана по спортивному ЧГК (2019)](#chgk_2019)
- [XI чемпионат Азербайджана по спортивному ЧГК (2016)](#chgk_2016)
- [X чемпионат Азербайджана по спортивному ЧГК (2015)](#chgk_2015)
- [IX чемпионат Азербайджана по спортивному ЧГК (2013)](#chgk_2013)
- [VIII чемпионат Азербайджана по спортивному ЧГК (2012)](#chgk_2012)
- [VII чемпионат Азербайджана по спортивному ЧГК (2008)](#chgk_2008)
- [VI чемпионат Азербайджана по спортивному ЧГК (2007)](#chgk_2007)
- [V чемпионат Азербайджана по спортивному ЧГК (2006)](#chgk_2006)
- [IV чемпионат Азербайджана по спортивному ЧГК (2005)](#chgk_2005)
- [III чемпионат Азербайджана по спортивному ЧГК (2004)](#chgk_2004)
- [II чемпионат Азербайджана по спортивному ЧГК (2003)](#chgk_2003)
- [I чемпионат Азербайджана по спортивному ЧГК (2002)](#chgk_2002)


**XVI чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 26 апреля 2026 года в Баку. <a id="chgk_2026"></a>

Победитель: **[«М4А1» (Баку)](https://rating.chgk.info/teams/40131)**
- Владимир Бабиор
- Анна Гаузер
- Джамиль Ализаде
- Кянан Гурбатли
- Мурад Ахундов
- Сеймур Агаев

Второе место заняла команда [«Поминки по финикам»](https://rating.chgk.info/teams/67979) (Баку), третье — [«Jazz»](https://rating.chgk.info/teams/45599) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12349). Больше информации о турнире — [в этом телеграм-канале](https://t.me/default_playground/361) и [здесь](https://t.me/chgknews/1432).

*[К оглавлению](#chgk_contents)*

---

**XV чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 25 мая 2025 года в Баку. <a id="chgk_2025"></a>

Победитель: **[«М4А1» (Баку)](https://rating.chgk.info/teams/40131)**
- Гейдар Гамзаев
- Елизавета Ежергина
- Джамиль Ализаде
- Кянан Гурбатли
- Мурад Ахундов
- Евгений Томашевский

Второе место заняла команда [«Jazz»](https://rating.chgk.info/teams/45599) (Баку), третье — [«Поминки по финикам»](https://rating.chgk.info/teams/67979) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11016), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/6510). Больше информации о турнире — [в этом телеграм-канале](https://t.me/default_playground/261) и [здесь](https://t.me/chgknews/1160).

*[К оглавлению](#chgk_contents)*

---

**XIV чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 21 апреля 2024 года в Баку. <a id="chgk_2024"></a>

Победитель: **[«Brainstorm» (Баку)](https://rating.chgk.info/teams/6074)**
- Яна Лялякина
- Малик Рамазанзаде
- Кёнуль Мамедова
- Ильхам Кумбатов
- Акпер Дадашлы
- Аббас Ахундов

Второе место заняла команда [«Поминки по финикам»](https://rating.chgk.info/teams/67979) (Баку), третье — [«Jazz»](https://rating.chgk.info/teams/45599) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/9897), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/5927). Больше информации о турнире — [здесь](https://t.me/chgknews/802).

*[К оглавлению](#chgk_contents)*

---

**XIII чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 5 февраля 2023 года в Баку. <a id="chgk_2023"></a>

Победитель: **[«Поминки по финикам» (Баку)](https://rating.chgk.info/teams/67979)**
- Эльнур Гасымзаде
- Малик Рамазанзаде
- Эльман Талыбов
- Саид Садыхов
- Роман Оркодашвили
- Азиз Муршудли

Второе место заняла команда [«Brainstorm»](https://rating.chgk.info/teams/6074) (Баку), третье — [«Jazz»](https://rating.chgk.info/teams/45599) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/8560), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/5597). Больше информации о турнире — [здесь](https://t.me/chgknews/428).

*[К оглавлению](#chgk_contents)*

---

**XII чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 14 апреля 2019 года в Баку. <a id="chgk_2019"></a>

Победитель: **[«Команда Гусейнова» (Баку)](https://rating.chgk.info/teams/299)**
- Борис Царицын
- Эмиль Мадатов
- Эмиль Исмаилов
- Фаик Гусейнов
- Теймур Гулиев
- Джамиля Азизова

Второе место заняла команда [«Команда Касумова»](https://rating.chgk.info/teams/243) (Баку), третье — [«Brainstorm»](https://rating.chgk.info/teams/6074) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5573), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/90).

*[К оглавлению](#chgk_contents)*

---

**XI чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 11 декабря 2016 года в Баку. <a id="chgk_2016"></a>

Победитель: **[«Brainstorm» (Баку)](https://rating.chgk.info/teams/6074)**
- Илья Мурзинов
- Эмин Расулзаде
- Яна Лялякина
- Ильхам Кумбатов
- Акпер Дадашлы
- Хафиз Гайыб
- Аббас Ахундов

Второе место заняла команда [«Команда Касумова»](https://rating.chgk.info/teams/243) (Баку), третье — [«КиПЛ»](https://rating.chgk.info/teams/5842) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4148), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/1081).

*[К оглавлению](#chgk_contents)*

---

**X чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 3 мая 2015 года в Баку. <a id="chgk_2015"></a>

Победитель: **[«Команда Гусейнова» (Баку)](https://rating.chgk.info/teams/299)**
- Джамиль Салманов
- Роман Оркодашвили
- Эмиль Мадатов
- Фаик Гусейнов
- Джамиля Азизова
- Руфат Абдулла

Второе место заняла команда [«Слон в удаве»](https://rating.chgk.info/teams/6075) (Баку), третье — [«КиПЛ»](https://rating.chgk.info/teams/5842) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3350), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/1816).

*[К оглавлению](#chgk_contents)*

---

**IX чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 18 мая 2013 года в Баку. <a id="chgk_2013"></a>

Победитель: **[«Команда Касумова» (Баку)](https://rating.chgk.info/teams/243)**
- Алексей Уланов
- Эльман Талыбов
- Рауф Наджафли
- Азиз Муршудли
- Балаш Касумов
- Аднан Ахундов
- Анар Азимов

Второе место заняла команда [«Эверест»](https://rating.chgk.info/teams/6521) (Баку), третье — [«Команда Гусейнова»](https://rating.chgk.info/teams/299) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2266), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/2729).

*[К оглавлению](#chgk_contents)*

---

**VIII чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 8 июня 2012 года в Баку. <a id="chgk_2012"></a>

Победитель: **[«Команда Касумова» (Баку)](https://rating.chgk.info/teams/243)**
- Алексей Уланов
- Эльман Талыбов
- Рауф Наджафли
- Азиз Муршудли
- Балаш Касумов
- Аднан Ахундов
- Анар Азимов

Второе место заняла команда [«Команда Гусейнова»](https://rating.chgk.info/teams/299) (Баку), третье — [«Слон в удаве»](https://rating.chgk.info/teams/6075) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2130), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3069). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/201206Baku.html).

*[К оглавлению](#chgk_contents)*

---

**VII чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 9–10 мая 2008 года в Баку. <a id="chgk_2008"></a>

Победитель: **[«Команда Касумова» (Баку)](https://rating.chgk.info/teams/243)**
- Рауф Наджафли
- Балаш Касумов
- Анар Гулиев
- Аднан Ахундов
- Ровшан Аскеров
- Анар Азимов
- Дмитрий Авдеенко

Второе место заняла команда [«Команда Гусейнова»](https://rating.chgk.info/teams/299) (Баку), третье — [«ТН»](https://rating.chgk.info/teams/1611) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/338). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/200805Baku.html).

*[К оглавлению](#chgk_contents)*

---

**VI чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 4 мая 2007 года в Баку. <a id="chgk_2007"></a>

Победитель: **[«Yo!J» (Баку)](https://rating.chgk.info/teams/2723)**
- Джахангир Фараджуллаев
- Эльман Талыбов
- Анар Наджафли
- Азиз Муршудли
- Елена Захарова
- Теймур Алиев

Второе место заняла команда [«Команда Касумова»](https://rating.chgk.info/teams/243) (Баку), третье — [«Команда Гусейнова»](https://rating.chgk.info/teams/299) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/242), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4635). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/200705Baku.html).

*[К оглавлению](#chgk_contents)*

---

**V чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 17 июня 2006 года в Баку. <a id="chgk_2006"></a>

Победитель: **[«Команда Гусейнова» (Баку)](https://rating.chgk.info/teams/299)**
- Роман Оркодашвили
- Эмиль Мадатов
- Фаик Гусейнов
- Илья Гинзбург
- Назлы Ахмедова
- Джамиля Азизова

Второе место заняла команда [«Yo!J»](https://rating.chgk.info/teams/2723) (Баку), третье — [«Команда Касумова»](https://rating.chgk.info/teams/243) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/147), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4360). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/200606Baku.html).

*[К оглавлению](#chgk_contents)*

---

**IV чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 4 июня 2005 года в Баку. <a id="chgk_2005"></a>

Победитель: **[«Команда Гусейнова» (Баку)](https://rating.chgk.info/teams/299)**
- Роман Оркодашвили
- Эмиль Мадатов
- Фаик Гусейнов
- Илья Гинзбург
- Анар Азимов
- Джамиля Азизова

Второе место заняла команда [«Команда Касумова»](https://rating.chgk.info/teams/243) (Баку), третье — [«Команда Мусаева»](https://rating.chgk.info/teams/543) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/107), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4007). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/200506Baku.html).

*[К оглавлению](#chgk_contents)*

---

**III чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 8 мая 2004 года в Баку. <a id="chgk_2004"></a>

Победитель: **[«Команда Касумова» (Баку)](https://rating.chgk.info/teams/243)**
- Рауф Наджафли
- Балаш Касумов
- Анар Гулиев
- Аднан Ахундов
- Ровшан Аскеров
- Дмитрий Авдеенко

Второе место разделили команды [«Команда Азимова»](https://rating.chgk.info/teams/242) (Баку), [«Команда Алиева»](https://rating.chgk.info/teams/268) (Баку) и [«Команда Гусейнова»](https://rating.chgk.info/teams/299) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/42), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3486). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/200405Baku.html).

*[К оглавлению](#chgk_contents)*

---

**II чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 10 мая 2003 года в Баку. <a id="chgk_2003"></a>

Победитель: **[«Команда Гусейнова» (Баку)](https://rating.chgk.info/teams/299)**
- Хафиз Гаибов
- Ильхам Гумбатов
- Шахин Мургузов
- Эмиль Мадатов
- Фаик Гусейнов
- Джамиля Азизова

Второе место заняла команда [«Команда Азимова»](https://rating.chgk.info/teams/242) (Баку), третье — [«Команда Алиева»](https://rating.chgk.info/teams/268) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1395). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/200305Baku.html).

*[К оглавлению](#chgk_contents)*

---

**I чемпионат Азербайджана по спортивному «Что? Где? Когда?»** прошёл 3–4 мая 2002 года в Баку. <a id="chgk_2002"></a>

Победитель: **[«Команда Касумова» (Баку)](https://rating.chgk.info/teams/243)**
- Фуад Мусаев
- Фариз Рзаев
- Роман Аллояров
- Рауф Наджафли
- Балаш Касумов
- Анар Гулиев
- Джейхун Гейбатов
- Эльнур Амикишиев

Второе место заняла команда [«Команда Азимова»](https://rating.chgk.info/teams/242) (Баку), третье — [«Команда Гусейнова»](https://rating.chgk.info/teams/299) (Баку).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1304).

*[К оглавлению](#chgk_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-brain"></div>

<a id="game-brain"></a><a id="brain_contents" name="brain_contents"></a>

- [IV чемпионат Азербайджана по БР (2005)](#brain_2005)
- [I чемпионат Азербайджана по БР (2001)](#brain_2001)


**IV чемпионат Азербайджана по брейн-рингу** прошёл 24–25 декабря 2005 года в Баку. <a id="brain_2005"></a>

Победитель: **[«Огуз» (Баку)](https://rating.chgk.info/teams/487)**
- Октай Магеррамов
- Юрий Чернов
- Эльдар Адильзаде
- Рустам Рустамов
- Абдулазим Гусейнов
- Илькин Етирмишли

Второе место заняла команда [«Команда Бабаева»](https://rating.chgk.info/teams/2271) (Баку), третье — [«Yo!J»](https://rating.chgk.info/teams/2723) (Баку). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/200512Baku.html).

*[К оглавлению](#brain_contents)*

---

**I чемпионат Азербайджана по брейн-рингу** прошёл 22–23 декабря 2001 года в Баку. <a id="brain_2001"></a>

Победитель: **[«Команда Лятифова» (Баку)](https://rating.chgk.info/teams/32752)**

*Состав команды [«Команда Лятифова»](https://rating.chgk.info/teams/32752) (Баку) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Команда Гусейнова»](https://rating.chgk.info/teams/299) (Баку). Третье место разделили команды [«Команда Зейналова»](https://rating.chgk.info/teams/33236) (Баку) и [«Команда Рагимова»](https://rating.chgk.info/teams/32841) (Баку). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/200112Baku.html).

*[К оглавлению](#brain_contents)*

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
<tr><td>2004</td><td><a href="https://rating.chgk.info/tournament/42">III чемпионат Азербайджана по ЧГК</a></td><td>неизвестны составы обладателей второго и третьего мест.</td></tr>
<tr><td>2003</td><td><a href="https://rating.chgk.info/tournament/1395">II чемпионат Азербайджана по ЧГК</a></td><td>неизвестны составы обладателей второго и третьего мест.</td></tr>
<tr><td>2002</td><td><a href="https://rating.chgk.info/tournament/1304">I чемпионат Азербайджана по ЧГК</a></td><td>неизвестны составы обладателей второго и третьего мест.</td></tr>
<tr><td>2001</td><td>I чемпионат Азербайджана по БР</td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
