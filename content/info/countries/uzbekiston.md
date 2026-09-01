---
title: Узбекистан
weight: 1
bookToC: false
---

# Узбекистан

Чемпионаты Узбекистана проводятся с 2004 года. Ниже можно увидеть статистику по всем призёрам — как командам, так и игрокам. Также в отдельных вкладках можно найти информацию о чемпионатах страны по той или иной дисциплине. \n\nСейчас не хватает информации о самом первом чемпионате Узбекистана, а также о ряде других турниров. Если вы что-то знаете о призёрах или их составах, напишите, пожалуйста, на почту <chgknews.info@gmail.com>.

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-kvrm" aria-selected="false">Турниры по КВРМ</button><button type="button" role="tab" data-tab="game-brain" aria-selected="false">Турниры по БР</button><button type="button" role="tab" data-tab="game-ek" aria-selected="false">Турниры по ЭК</button><button type="button" role="tab" data-tab="game-hamsa" aria-selected="false">Турниры по «Хамсе»</button><button type="button" role="tab" data-tab="game-ssi" aria-selected="false">Турниры по ССИ</button><button type="button" role="tab" data-tab="missing-data" aria-selected="false">Проблемы</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th rowspan="2">Команда</th><th rowspan="2">Город</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">КВРМ</th><th colspan="3" style="text-align:center">БР</th><th colspan="3" style="text-align:center">«Хамса»</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/2462">Мы</a></td>
<td>Ташкент</td>
<td>3</td>
<td>9</td>
<td>3</td>
<td>15</td>
<td>3</td>
<td>7</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/4864">НМТТ (Никита Мобайл ТэТэ)</a></td>
<td>Ташкент</td>
<td>6</td>
<td>3</td>
<td>1</td>
<td>10</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/4156">7Hz</a></td>
<td>Ташкент</td>
<td>4</td>
<td>2</td>
<td>4</td>
<td>10</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/2909">Мистерия</a></td>
<td>Ташкент</td>
<td>7</td>
<td>2</td>
<td>0</td>
<td>9</td>
<td>6</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/28587">Пахтакор</a></td>
<td>Ташкент</td>
<td>0</td>
<td>2</td>
<td>6</td>
<td>8</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/5858">Sonet (DimTeam)</a></td>
<td>Ташкент</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/4749">ParadoX</a></td>
<td>Навои</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3449">Veni Vidi Vici</a></td>
<td>Ташкент</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/59318">КАД</a></td>
<td>Ташкент</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/62494">Котовского 26 кв 58</a></td>
<td>Ташкент</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/46377">НЗ</a></td>
<td>сборная</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/815">Брюссельские</a></td>
<td>Ташкент</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/98988">Комната</a></td>
<td>Ташкент</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3523">Заковат-1</a></td>
<td>Ташкент</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3687">Dream team</a></td>
<td>Ташкент</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/92163">Императив релоканта</a></td>
<td>Ташкент</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/62644">Ход конём</a></td>
<td>Ташкент</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="players"></div>

<a id="players"></a>

<table>
<thead>
<tr><th rowspan="2">Игрок</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">ЧГК</th><th colspan="3" style="text-align:center">БР</th><th colspan="3" style="text-align:center">ССИ</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/player/18316">Александр Ли</a></td>
<td>3</td>
<td>4</td>
<td>2</td>
<td>9</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26586">Александр Райков</a></td>
<td>2</td>
<td>6</td>
<td>1</td>
<td>9</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>5</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12482">Акрам Икрамов</a></td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>7</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/535">Алексей Акименко</a></td>
<td>2</td>
<td>3</td>
<td>2</td>
<td>7</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25981">Галина Прибыткова</a></td>
<td>2</td>
<td>4</td>
<td>0</td>
<td>6</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28654">Артём Семёнов</a></td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32901">Наиль Фарукшин</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8986">Наталья Дейнека</a></td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>5</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9240">Абдулазиз Джалилов</a></td>
<td>1</td>
<td>0</td>
<td>4</td>
<td>5</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2673">Хаким Батыралиев</a></td>
<td>0</td>
<td>2</td>
<td>3</td>
<td>5</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27852">Ян Садковский</a></td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/41902">Валерий Ким</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/487">Игорь Аипкин</a></td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7215">Игорь Глущенко</a></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37142">Азизбек Юсуфов</a></td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9801">Егор Дружинин</a></td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28281">Алексей Саркулов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/87499">Наринэ Багдасарян</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/75101">Станислав Чиревко</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11220">Аскар Заитов</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/95596">Василий Щедрин</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13674">Алексей Карцевич</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4812">Дмитрий Вагапов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4337">Антонина Бударина</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14394">Владимир Клименко</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19275">Никита Макаренко</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30579">Герман Стимбан</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27827">Дина Сагадиева</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35643">Усман Шарифходжаев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13782">Тимур Кафиатуллин</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9299">Отабек Джураев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37222">Валерия Якимова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/66802">Галина Никитина</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13196">Евгений Калюков</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35753">Лейла Шахназарова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/75099">Сардор Ахмедов</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36821">Сергей Щербаков</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/101499">Мурод Абдукамилов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32589">Вадим Улитчев</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/48843">Мурод Хамраев</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35750">Георгий Шахназаров</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37252">Пётр Яковлев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30537">Игорь Степанян</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/174012">Павел Корнилов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/171621">Алексей Грачёв</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12088">Алексей Иванов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/150487">Барно Джалилова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/160060">Бобур Каримов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32496">Дарья Тян</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54897">Динара Адылова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/164186">Павел Логинов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/169757">Роман Башлыков</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21877">Рустам Мурзаханов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/101500">Эльбек Нурмухамедов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/131786">Георгий Шванов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4339">Елена Бударина</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13535">Руслан Каримов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
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
<div class="country-tab-start" data-tab="game-kvrm"></div>

<a id="game-kvrm"></a><a id="kvrm_contents" name="kvrm_contents"></a>

- [V чемпионат Узбекистана по «Заковату» (2026)](#zakovat_2026)
- [IV чемпионат Узбекистана по «Заковату» (2025)](#zakovat_2025)
- [III чемпионат Узбекистана по «Заковату» (2024)](#zakovat_2024)
- [II чемпионат Узбекистана по «Заковату» (2023)](#zakovat_2023)
- [I чемпионат Узбекистана по «Заковату» (2022)](#zakovat_2022)
- [XVI чемпионат Узбекистана по спортивному ЧГК (2019)](#chgk_2019)
- [XV чемпионат Узбекистана по спортивному ЧГК (2018)](#chgk_2018)
- [XIV чемпионат Узбекистана по спортивному ЧГК (2017)](#chgk_2017)
- [XIII чемпионат Узбекистана по спортивному ЧГК (2016)](#chgk_2016)
- [XII чемпионат Узбекистана по спортивному ЧГК (2015)](#chgk_2015)
- [XI чемпионат Узбекистана по спортивному ЧГК (2014)](#chgk_2014)
- [X чемпионат Узбекистана по спортивному ЧГК (2013)](#chgk_2013)
- [IX чемпионат Узбекистана по спортивному ЧГК (2012)](#chgk_2012)
- [VIII чемпионат Узбекистана по спортивному ЧГК (2011)](#chgk_2011)
- [VII чемпионат Узбекистана по спортивному ЧГК (2010)](#chgk_2010)
- [VI чемпионат Узбекистана по спортивному ЧГК (2009)](#chgk_2009)
- [V чемпионат Узбекистана по спортивному ЧГК (2008)](#chgk_2008)
- [IV чемпионат Узбекистана по спортивному ЧГК (2007)](#chgk_2007)
- [III чемпионат Узбекистана по спортивному ЧГК (2006)](#chgk_2006)
- [II чемпионат Узбекистана по спортивному ЧГК (2005)](#chgk_2005)
- [I чемпионат Узбекистана по спортивному ЧГК (2004)](#chgk_2004)


**V чемпионат Узбекистана по «Заковату»** прошёл 30–31 мая 2026 года в Ташкенте. <a id="zakovat_2026"></a>

Победитель: **[«Мистерия» (Ташкент)](https://rating.chgk.info/teams/2909)**

Второе место заняла команда [«КАД»](https://rating.chgk.info/teams/59318) (Ташкент), третье — [«Комната»](https://rating.chgk.info/teams/98988) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/13657).

*[К оглавлению](#kvrm_contents)*

---

**IV чемпионат Узбекистана по «Заковату»** прошёл 7–8 июня 2025 года в Ташкенте. <a id="zakovat_2025"></a>

Победитель: **[«Мистерия» (Ташкент)](https://rating.chgk.info/teams/2909)**

Второе место заняла команда [«Комната»](https://rating.chgk.info/teams/98988) (Ташкент), третье — [«КАД»](https://rating.chgk.info/teams/59318) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12039).

*[К оглавлению](#kvrm_contents)*

---

**III чемпионат Узбекистана по «Заковату»** прошёл 25 мая 2024 года в Ташкенте. <a id="zakovat_2024"></a>

Победитель: **[«Мистерия» (Ташкент)](https://rating.chgk.info/teams/2909)**

Второе место заняла команда [«Котовского 26 кв 58»](https://rating.chgk.info/teams/62494) (Ташкент), третье — [«Императив релоканта»](https://rating.chgk.info/teams/92163) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/10780).

*[К оглавлению](#kvrm_contents)*

---

**II чемпионат Узбекистана по «Заковату»** прошёл 14 мая 2023 года в Ташкенте. <a id="zakovat_2023"></a>

Победитель: **[«Котовского 26 кв 58» (Ташкент)](https://rating.chgk.info/teams/62494)**

Второе место заняла команда [«Мистерия»](https://rating.chgk.info/teams/2909) (Ташкент), третье — [«Пахтакор»](https://rating.chgk.info/teams/28587) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/9157).

*[К оглавлению](#kvrm_contents)*

---

**I чемпионат Узбекистана по «Заковату»** прошёл 21 августа 2022 года в Ташкенте. <a id="zakovat_2022"></a>

Победитель: **[«Мистерия» (Ташкент)](https://rating.chgk.info/teams/2909)**

Второе место заняла команда [«Пахтакор»](https://rating.chgk.info/teams/28587) (Ташкент), третье — [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/8287).

*[К оглавлению](#kvrm_contents)*

---

**XVI чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 27 октября 2019 года в Ташкенте. <a id="chgk_2019"></a>

Победитель: **[«Мистерия» (Ташкент)](https://rating.chgk.info/teams/2909)**
- Мурод Абдукамилов
- Наринэ Багдасарян
- Артём Семёнов
- Ян Садковский
- Акрам Икрамов
- Игорь Аипкин

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент). Третье место разделили команды [«КАД»](https://rating.chgk.info/teams/59318) (Ташкент) и [«Ход конём»](https://rating.chgk.info/teams/62644) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5989).

*[К оглавлению](#kvrm_contents)*

---

**XV чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 21–22 апреля 2018 года в Ташкенте. <a id="chgk_2018"></a>

Победитель: **[«Мистерия» (Ташкент)](https://rating.chgk.info/teams/2909)**
- Наринэ Багдасарян
- Наиль Фарукшин
- Артём Семёнов
- Ян Садковский
- Акрам Икрамов
- Игорь Аипкин

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент). Третье место разделили команды [«7Hz»](https://rating.chgk.info/teams/4156) (Ташкент) и [«Пахтакор»](https://rating.chgk.info/teams/28587) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4745).

*[К оглавлению](#kvrm_contents)*

---

**XIV чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 23 апреля 2017 года в Ташкенте. <a id="chgk_2017"></a>

Победитель: **[«Мы» (Ташкент)](https://rating.chgk.info/teams/2462)**
- Василий Щедрин
- Станислав Чиревко
- Валерий Ким
- Дина Сагадиева
- Галина Прибыткова
- Александр Ли
- Наталья Дейнека
- Алексей Акименко

Второе место заняла команда [«Мистерия»](https://rating.chgk.info/teams/2909) (Ташкент), третье — [«DimTeam»](https://rating.chgk.info/teams/5858) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4197).

*[К оглавлению](#kvrm_contents)*

---

**XIII чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 21–22 мая 2016 года в Ташкенте. <a id="chgk_2016"></a>

Победитель: **[«Мы» (Ташкент)](https://rating.chgk.info/teams/2462)**
- Станислав Чиревко
- Валерий Ким
- Герман Стимбан
- Александр Райков
- Галина Прибыткова
- Александр Ли
- Аскар Заитов
- Наталья Дейнека

Второе место заняла команда [«7Hz»](https://rating.chgk.info/teams/4156) (Ташкент), третье — [«DimTeam»](https://rating.chgk.info/teams/5858) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3613).

*[К оглавлению](#kvrm_contents)*

---

**XII чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 28–29 марта 2015 года в Ташкенте. <a id="chgk_2015"></a>

Победитель: **[«Sonet» (Ташкент)](https://rating.chgk.info/teams/5858)**
- Азизбек Юсуфов
- Усман Шарифходжаев
- Алексей Карцевич
- Абдулазиз Джалилов
- Игорь Глущенко
- Дмитрий Вагапов

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент), третье — [«7Hz»](https://rating.chgk.info/teams/4156) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3253).

*[К оглавлению](#kvrm_contents)*

---

**XI чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 22–23 марта 2014 года в Ташкенте. <a id="chgk_2014"></a>

Победитель: **[«Sonet» (Ташкент)](https://rating.chgk.info/teams/5858)**

Второе место заняла команда [«НЗ»](https://rating.chgk.info/teams/46377) (сборная), третье — [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2826).

*[К оглавлению](#kvrm_contents)*

---

**X чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 20–21 апреля 2013 года в Ташкенте. <a id="chgk_2013"></a>

Победитель: **[«НМТТ» (Ташкент)](https://rating.chgk.info/teams/4864)**

Второе место заняла команда [«ParadoX»](https://rating.chgk.info/teams/4749) (Навои), третье — [«7Hz»](https://rating.chgk.info/teams/4156) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2362).

*[К оглавлению](#kvrm_contents)*

---

**IX чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 5–6 мая 2012 года в Ташкенте. <a id="chgk_2012"></a>

Победитель: **[«НМТТ» (Ташкент)](https://rating.chgk.info/teams/4864)**

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент), третье — [«Пахтакор»](https://rating.chgk.info/teams/28587) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2099).

*[К оглавлению](#kvrm_contents)*

---

**VIII чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 6–7 мая 2011 года в Ташкенте. <a id="chgk_2011"></a>

Победитель: **[«Никита Мобайл ТэТэ» (Ташкент)](https://rating.chgk.info/teams/4864)**

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент), третье — [«7Hz»](https://rating.chgk.info/teams/4156) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1775).

*[К оглавлению](#kvrm_contents)*

---

**VII чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 28–29 мая 2010 года в Ташкенте. <a id="chgk_2010"></a>

Победитель: **[«НМТТ» (Ташкент)](https://rating.chgk.info/teams/4864)**

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент), третье — [«ParadoX»](https://rating.chgk.info/teams/4749) (Навои).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/665).

*[К оглавлению](#kvrm_contents)*

---

**VI чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 9 мая 2009 года в Ташкенте. <a id="chgk_2009"></a>

Победитель: **[«7Hz» (Ташкент)](https://rating.chgk.info/teams/4156)**

Второе место заняла команда [«НМТТ»](https://rating.chgk.info/teams/4864) (Ташкент), третье — [«Брюссельские»](https://rating.chgk.info/teams/815) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/456).

*[К оглавлению](#kvrm_contents)*

---

**V чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 9–10 мая 2008 года в Ташкенте. <a id="chgk_2008"></a>

Победитель: **[«НМТТ» (Ташкент)](https://rating.chgk.info/teams/4864)**

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент), третье — [«Veni Vidi Vici»](https://rating.chgk.info/teams/3449) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/340).

*[К оглавлению](#kvrm_contents)*

---

**IV чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 5 мая 2007 года в Ташкенте. <a id="chgk_2007"></a>

Победитель: **[«7Hz» (Ташкент)](https://rating.chgk.info/teams/4156)**

Второе место заняла команда [«Veni Vidi Vici»](https://rating.chgk.info/teams/3449) (Ташкент), третье — [«НМТТ»](https://rating.chgk.info/teams/4864) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/243).

*[К оглавлению](#kvrm_contents)*

---

**III чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 13 мая 2006 года в Ташкенте. <a id="chgk_2006"></a>

Победитель: **[«7Hz» (Ташкент)](https://rating.chgk.info/teams/4156)**

Второе место заняла команда [«НМТТ»](https://rating.chgk.info/teams/4864) (Ташкент), третье — [«Dream team»](https://rating.chgk.info/teams/3687) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/169).

*[К оглавлению](#kvrm_contents)*

---

**II чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 23 апреля 2005 года в Ташкенте. <a id="chgk_2005"></a>

Победитель: **[«Брюссельские» (Ташкент)](https://rating.chgk.info/teams/815)**

Второе место заняла команда [«Заковат-1»](https://rating.chgk.info/teams/3523) (Ташкент), третье — [«Veni Vidi Vici»](https://rating.chgk.info/teams/3449) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/95).

*[К оглавлению](#kvrm_contents)*

---

**I чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл в 2004 году в Ташкенте. <a id="chgk_2004"></a>

Победитель: **[«Мы» (Ташкент)](https://rating.chgk.info/teams/2462)**


*[К оглавлению](#kvrm_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-brain"></div>

<a id="game-brain"></a><a id="brain_contents" name="brain_contents"></a>

- [VII чемпионат Узбекистана по БР (2015)](#brain_2015)
- [VI чемпионат Узбекистана по БР (2014)](#brain_2014)
- [V чемпионат Узбекистана по БР (2013)](#brain_2013)
- [IV чемпионат Узбекистана по БР (2012)](#brain_2012)
- [III чемпионат Узбекистана по БР (2011)](#brain_2011)
- [II чемпионат Узбекистана по БР (2009)](#brain_2009)


**VII чемпионат Узбекистана по брейн-рингу** прошёл 28–29 марта 2015 года в Ташкенте. <a id="brain_2015"></a>

Победитель: **[«Мистерия» (Ташкент)](https://rating.chgk.info/teams/2909)**
- Ян Садковский

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент), третье — [«Пахтакор»](https://rating.chgk.info/teams/28587) (Ташкент).

*[К оглавлению](#brain_contents)*

---

**VI чемпионат Узбекистана по брейн-рингу** прошёл 22–23 марта 2014 года в Ташкенте. <a id="brain_2014"></a>

Победитель: **[«НЗ» (сборная)](https://rating.chgk.info/teams/46377)**

Второе место заняла команда [«7Hz»](https://rating.chgk.info/teams/4156) (Ташкент), третье — [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент).

*[К оглавлению](#brain_contents)*

---

**V чемпионат Узбекистана по брейн-рингу** прошёл 20–21 апреля 2013 года в Ташкенте. <a id="brain_2013"></a>

Победитель: **[«ParadoX» (Навои)](https://rating.chgk.info/teams/4749)**

Второе место заняла команда [«НМТТ»](https://rating.chgk.info/teams/4864) (Ташкент), третье — [«Пахтакор»](https://rating.chgk.info/teams/28587) (Ташкент).

*[К оглавлению](#brain_contents)*

---

**IV чемпионат Узбекистана по брейн-рингу** прошёл 5–6 мая 2012 года в Ташкенте. <a id="brain_2012"></a>

Победитель: **[«НМТТ» (Ташкент)](https://rating.chgk.info/teams/4864)**

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент), третье — [«Пахтакор»](https://rating.chgk.info/teams/28587) (Ташкент).

*[К оглавлению](#brain_contents)*

---

**III чемпионат Узбекистана по брейн-рингу** прошёл 6–7 мая 2011 года в Ташкенте. Результаты пока не учтены в статистике. <a id="brain_2011"></a>

*[К оглавлению](#brain_contents)*

---

**II чемпионат Узбекистана по брейн-рингу** прошёл 8 мая 2009 года в Ташкенте. Результаты пока не учтены в статистике. <a id="brain_2009"></a>

*[К оглавлению](#brain_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ek"></div>

<a id="game-ek"></a><a id="ek_contents" name="ek_contents"></a>

- [I чемпионат Узбекистана по ЭК (2011)](#ek_2011)


**I чемпионат Узбекистана по эрудит-квартету** прошёл 6–7 мая 2011 года в Ташкенте. Результаты пока не учтены в статистике. <a id="ek_2011"></a>

*[К оглавлению](#ek_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-hamsa"></div>

<a id="game-hamsa"></a><a id="hamsa_contents" name="hamsa_contents"></a>

- [I чемпионат Узбекистана по «Хамсе» (2013)](#hamsa_2013)


**I чемпионат Узбекистана по «Хамсе»** прошёл 20–21 апреля 2013 года в Ташкенте. <a id="hamsa_2013"></a>

Победитель: **[«7Hz» (Ташкент)](https://rating.chgk.info/teams/4156)**

Второе место заняла команда [«Пахтакор»](https://rating.chgk.info/teams/28587) (Ташкент), третье — [«ParadoX»](https://rating.chgk.info/teams/4749) (Навои).

*[К оглавлению](#hamsa_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ssi"></div>

<a id="game-ssi"></a><a id="ssi_contents" name="ssi_contents"></a>

- [XV чемпионат Узбекистана по ССИ (2026)](#ssi_2026)
- [XIV чемпионат Узбекистана по ССИ (2025)](#ssi_2025)
- [XIII чемпионат Узбекистана по ССИ (2024)](#ssi_2024)
- [XII чемпионат Узбекистана по ССИ (2023)](#ssi_2023)
- [XI чемпионат Узбекистана по ССИ (2022)](#ssi_2022)
- [X чемпионат Узбекистана по ССИ (2021)](#ssi_2021)
- [IX чемпионат Узбекистана по ССИ (2019)](#ssi_2019)
- [VIII чемпионат Узбекистана по ССИ (2016)](#ssi_2016)
- [VII чемпионат Узбекистана по ССИ (2015)](#ssi_2015)
- [VI чемпионат Узбекистана по ССИ (2014)](#ssi_2014)
- [V чемпионат Узбекистана по ССИ (2013)](#ssi_2013)
- [IV чемпионат Узбекистана по ССИ (2012)](#ssi_2012)
- [III чемпионат Узбекистана по ССИ (2010)](#ssi_2010)
- [II чемпионат Узбекистана по ССИ (2009)](#ssi_2009)
- [I чемпионат Узбекистана по ССИ (2007)](#ssi_2007)


**XV чемпионат Узбекистана по спортивной «Своей игре»** прошёл 21 февраля 2026 года в Ташкенте. <a id="ssi_2026"></a>

Победитель: **[Артём Семёнов](https://rating.chgk.info/player/28654)**

Второе место занял [Александр Ли](https://rating.chgk.info/player/18316), третье — [Егор Дружинин](https://rating.chgk.info/player/9801).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1Qr7GOSy2jy-oiloNYhx83lz4mvmrUcoeDUVDPT3yRiQ/edit?gid=1573363467#gid=1573363467). Больше информации о турнире — [здесь](https://t.me/chgknews/1375).

*[К оглавлению](#ssi_contents)*

---

**XIV чемпионат Узбекистана по спортивной «Своей игре»** прошёл 25 января 2025 года в Ташкенте. <a id="ssi_2025"></a>

Победитель: **[Тимур Кафиатуллин](https://rating.chgk.info/player/13782)**

Второе место занял [Павел Корнилов](https://rating.chgk.info/player/174012), третье — [Егор Дружинин](https://rating.chgk.info/player/9801).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1obYf9XLtdzMaUCsyclm8ePN3-WwJpYDlwt4_iqg4JwQ/edit?gid=1573363467#gid=1573363467). Больше информации о турнире — [здесь](https://t.me/chgknews/1027).

*[К оглавлению](#ssi_contents)*

---

**XIII чемпионат Узбекистана по спортивной «Своей игре»** прошёл 16 марта 2024 года в Ташкенте. <a id="ssi_2024"></a>

Победитель: **[Александр Ли](https://rating.chgk.info/player/18316)**

Второе место занял [Егор Дружинин](https://rating.chgk.info/player/9801), третье — [Тимур Кафиатуллин](https://rating.chgk.info/player/13782).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1fQ8xiH6y5hiwnn_eqgdSTYIdYFR6X0mkCON7PfgT7h8/edit?usp=sharing). Больше информации о турнире — [здесь](https://t.me/chgknews/765).

*[К оглавлению](#ssi_contents)*

---

**XII чемпионат Узбекистана по спортивной «Своей игре»** прошёл 23 февраля 2023 года в Ташкенте. <a id="ssi_2023"></a>

Победитель: **[Акрам Икрамов](https://rating.chgk.info/player/12482)**

Второе место занял [Егор Дружинин](https://rating.chgk.info/player/9801), третье — [Александр Ли](https://rating.chgk.info/player/18316).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1rzY7x0JCcM9Yaa0lBlAhJCEP5vY2sELek_5F554M9Cg/edit#gid=1573363467). Больше информации о турнире — [в этом телеграм-канале](https://t.me/iivtiivt/52) и [здесь](https://t.me/chgknews/442).

*[К оглавлению](#ssi_contents)*

---

**XI чемпионат Узбекистана по спортивной «Своей игре»** прошёл 6 февраля 2022 года в Ташкенте. <a id="ssi_2022"></a>

Победитель: **[Артём Семёнов](https://rating.chgk.info/player/28654)**

Второе место занял [Акрам Икрамов](https://rating.chgk.info/player/12482), третье — [Александр Ли](https://rating.chgk.info/player/18316). Больше информации о турнире — [в этом телеграм-канале](https://t.me/auluz/297).

*[К оглавлению](#ssi_contents)*

---

**X чемпионат Узбекистана по спортивной «Своей игре»** прошёл 31 января 2021 года в Ташкенте. <a id="ssi_2021"></a>

Победитель: **[Акрам Икрамов](https://rating.chgk.info/player/12482)**

Второе место занял [Александр Райков](https://rating.chgk.info/player/26586), третье — [Георгий Шванов](https://rating.chgk.info/player/131786). Больше информации о турнире — [в этом телеграм-канале](https://t.me/auluz/271).

*[К оглавлению](#ssi_contents)*

---

**IX чемпионат Узбекистана по спортивной «Своей игре»** прошёл 15 декабря 2019 года в Ташкенте. <a id="ssi_2019"></a>

Победитель: **[Акрам Икрамов](https://rating.chgk.info/player/12482)**

Второе место занял [Игорь Аипкин](https://rating.chgk.info/player/487), третье — [Сардор Ахмедов](https://rating.chgk.info/player/75099). Больше информации о турнире — [в этом телеграм-канале](https://t.me/auluz/224).

*[К оглавлению](#ssi_contents)*

---

**VIII чемпионат Узбекистана по спортивной «Своей игре»** прошёл 21–22 мая 2016 года в Ташкенте. <a id="ssi_2016"></a>

Победитель: **[Алексей Акименко](https://rating.chgk.info/player/535)**

*На этом турнире часть призёров неизвестна. Если вы что-то о них знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

*[К оглавлению](#ssi_contents)*

---

**VII чемпионат Узбекистана по спортивной «Своей игре»** прошёл 28–29 марта 2015 года в Ташкенте. <a id="ssi_2015"></a>

Победитель: **[Наиль Фарукшин](https://rating.chgk.info/player/32901)**

Второе место занял [Александр Райков](https://rating.chgk.info/player/26586), третье — [Алексей Акименко](https://rating.chgk.info/player/535).

*[К оглавлению](#ssi_contents)*

---

**VI чемпионат Узбекистана по спортивной «Своей игре»** прошёл 22–23 марта 2014 года в Ташкенте. <a id="ssi_2014"></a>

Победитель: **[Наиль Фарукшин](https://rating.chgk.info/player/32901)**

Второе место занял [Александр Райков](https://rating.chgk.info/player/26586), третье — [Азизбек Юсуфов](https://rating.chgk.info/player/37142).

*[К оглавлению](#ssi_contents)*

---

**V чемпионат Узбекистана по спортивной «Своей игре»** прошёл 20–21 апреля 2013 года в Ташкенте. <a id="ssi_2013"></a>

Победитель: **[Герман Стимбан](https://rating.chgk.info/player/30579)**

Второе место занял [Хаким Батыралиев](https://rating.chgk.info/player/2673), третье — [Абдулазиз Джалилов](https://rating.chgk.info/player/9240).

*[К оглавлению](#ssi_contents)*

---

**IV чемпионат Узбекистана по спортивной «Своей игре»** прошёл 5–6 мая 2012 года в Ташкенте. <a id="ssi_2012"></a>

Победитель: **[Мурод Хамраев](https://rating.chgk.info/player/48843)**

Второе место занял [Александр Райков](https://rating.chgk.info/player/26586), третье — [Сергей Щербаков](https://rating.chgk.info/player/36821).

*[К оглавлению](#ssi_contents)*

---

**III чемпионат Узбекистана по спортивной «Своей игре»** прошёл 12 декабря 2010 года в Ташкенте. <a id="ssi_2010"></a>

Победитель: **[Александр Райков](https://rating.chgk.info/player/26586)**

Второе место занял [Игорь Степанян](https://rating.chgk.info/player/30537).

*На этом турнире часть призёров неизвестна. Если вы что-то о них знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

*[К оглавлению](#ssi_contents)*

---

**II чемпионат Узбекистана по спортивной «Своей игре»** прошёл 13 декабря 2009 года в Ташкенте. <a id="ssi_2009"></a>

Победитель: **[Вадим Улитчев](https://rating.chgk.info/player/32589)**

Второе место занял [Александр Райков](https://rating.chgk.info/player/26586), третье — [Руслан Каримов](https://rating.chgk.info/player/13535).

*[К оглавлению](#ssi_contents)*

---

**I чемпионат Узбекистана по спортивной «Своей игре»** прошёл 7 июля 2007 года в Ташкенте. <a id="ssi_2007"></a>

Победитель: **[Игорь Глущенко](https://rating.chgk.info/player/7215)**

Второе место занял [Галина Прибыткова](https://rating.chgk.info/player/25981), третье — [Елена Бударина](https://rating.chgk.info/player/4339).

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
<tr><td>2016</td><td>VIII чемпионат Узбекистана по ССИ</td><td>неизвестны обладатели второго и третьего мест.</td></tr>
<tr><td>2011</td><td>III чемпионат Узбекистана по БР</td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2011</td><td>I чемпионат Узбекистана по ЭК</td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2010</td><td>III чемпионат Узбекистана по ССИ</td><td>неизвестен обладатель третьего места.</td></tr>
<tr><td>2009</td><td>II чемпионат Узбекистана по БР</td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2004</td><td>I чемпионат Узбекистана по ЧГК</td><td>неизвестны составы обладателей второго и третьего мест, точная дата проведения турнира.</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
