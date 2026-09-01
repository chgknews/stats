---
title: Казахстан
weight: 1
bookToC: false
---

# Казахстан

Чемпионаты Казахстана проводятся с 2011 года. Ниже можно увидеть статистику по всем призёрам — как командам, так и игрокам. Также в отдельных вкладках можно найти информацию о чемпионатах страны по той или иной дисциплине.

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-kvrm" aria-selected="false">Турниры по КВРМ</button><button type="button" role="tab" data-tab="game-brain" aria-selected="false">Турниры по БР</button><button type="button" role="tab" data-tab="game-hamsa" aria-selected="false">Турниры по «Хамсе»</button><button type="button" role="tab" data-tab="game-ssi" aria-selected="false">Турниры по ССИ</button><button type="button" role="tab" data-tab="missing-data" aria-selected="false">Нет данных</button></nav>
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
<td><a href="https://rating.chgk.info/teams/41492">Бедлам (Север Помнит)</a></td>
<td>Астана</td>
<td>5</td>
<td>7</td>
<td>2</td>
<td>14</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/27684">Brain Art</a></td>
<td>Алматы</td>
<td>3</td>
<td>4</td>
<td>6</td>
<td>13</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/42100">Резко континентальные</a></td>
<td>Астана</td>
<td>2</td>
<td>6</td>
<td>4</td>
<td>12</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/49225">Команда Игоря Пятова (Quantum / Ничоси)</a></td>
<td>Алматы</td>
<td>5</td>
<td>0</td>
<td>3</td>
<td>8</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/89600">Ангел в тюбетейке (Осторожно, надвигается кайфун)</a></td>
<td>Астана</td>
<td>4</td>
<td>1</td>
<td>3</td>
<td>8</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/37797">Эрудит (Элизабет Пэрриш)</a></td>
<td>Алматы</td>
<td>2</td>
<td>4</td>
<td>2</td>
<td>8</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/27683">Альфа</a></td>
<td>Алматы</td>
<td>4</td>
<td>1</td>
<td>2</td>
<td>7</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/88108">Простые работяги</a></td>
<td>Алматы</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>5</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/93605">Интеллект-экипаж</a></td>
<td>Алматы</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>5</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/27685">Крылья Гавриила</a></td>
<td>Алматы</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/65159">И никого не стало</a></td>
<td>Алматы</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/76272">Приятные люди</a></td>
<td>Астана</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/93518">Элизабет Пэрриш</a></td>
<td>Алматы</td>
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
<td><a href="https://rating.chgk.info/teams/45560">ДНК (Тропик Рака)</a></td>
<td>Астана</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/38145">Каспий</a></td>
<td>Актау</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/39765">Анкор</a></td>
<td>Актау</td>
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
<td><a href="https://rating.chgk.info/teams/27429">No Буратинос</a></td>
<td>Астана</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/37654">Glory</a></td>
<td>Алматы</td>
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
<td><a href="https://rating.chgk.info/teams/42320">Poker Face</a></td>
<td>Караганда</td>
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
<td><a href="https://rating.chgk.info/teams/68172">Басенджи</a></td>
<td>Алматы</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/91998">Первый номер драфта</a></td>
<td>Астана</td>
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
<td><a href="https://rating.chgk.info/teams/91036">Рецессивный доминант</a></td>
<td>Астана</td>
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
<td><a href="https://rating.chgk.info/teams/7570">Страх и ненависть в Майкудуке</a></td>
<td>Караганда</td>
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
<td><a href="https://rating.chgk.info/teams/42364">Der Рефрижератор</a></td>
<td>Караганда</td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/59835">Вжух</a></td>
<td>Алматы</td>
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
<div class="country-tab-start" data-tab="players"></div>

<a id="players"></a>

<table>
<thead>
<tr><th rowspan="2">Игрок</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">КВРМ</th><th colspan="3" style="text-align:center">БР</th><th colspan="3" style="text-align:center">«Хамса»</th><th colspan="3" style="text-align:center">ССИ</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/player/51715">Анвар Мухаметкалиев</a></td>
<td>22</td>
<td>6</td>
<td>6</td>
<td>34</td>
<td>4</td>
<td>4</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>2</td>
<td>7</td>
<td>1</td>
<td>1</td>
<td>7</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51774">Антон Горский</a></td>
<td>11</td>
<td>8</td>
<td>6</td>
<td>25</td>
<td>5</td>
<td>4</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>2</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/59147">Азат Тургунов</a></td>
<td>10</td>
<td>8</td>
<td>7</td>
<td>25</td>
<td>3</td>
<td>5</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>4</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/57032">Мольдер Рубанова</a></td>
<td>8</td>
<td>4</td>
<td>8</td>
<td>20</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>4</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51733">Валерий Володин</a></td>
<td>13</td>
<td>2</td>
<td>4</td>
<td>19</td>
<td>3</td>
<td>2</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>7</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/122503">Валерий Есаулков</a></td>
<td>9</td>
<td>6</td>
<td>4</td>
<td>19</td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2885">Бауржан Бектемиров</a></td>
<td>7</td>
<td>6</td>
<td>5</td>
<td>18</td>
<td>4</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71772">Муслима Карабалаева</a></td>
<td>6</td>
<td>8</td>
<td>4</td>
<td>18</td>
<td>5</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51751">Дария Жылкыбаева (Ибрагимова)</a></td>
<td>9</td>
<td>2</td>
<td>6</td>
<td>17</td>
<td>6</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29607">Герман Смирнов</a></td>
<td>10</td>
<td>1</td>
<td>5</td>
<td>16</td>
<td>5</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/61905">Тимур Шайткалиев</a></td>
<td>6</td>
<td>4</td>
<td>5</td>
<td>15</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51725">Чингиз Жылкыбаев</a></td>
<td>3</td>
<td>4</td>
<td>7</td>
<td>14</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54668">Данияр Алпысбай</a></td>
<td>4</td>
<td>6</td>
<td>3</td>
<td>13</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71780">Эльдар Бейсимбеков</a></td>
<td>2</td>
<td>8</td>
<td>3</td>
<td>13</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71773">Руслан Жолсеитов</a></td>
<td>5</td>
<td>5</td>
<td>2</td>
<td>12</td>
<td>3</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/53701">Фарит Алиби</a></td>
<td>2</td>
<td>7</td>
<td>3</td>
<td>12</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71809">Мария Сеилова</a></td>
<td>2</td>
<td>6</td>
<td>4</td>
<td>12</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51719">Валерия Вознесенская</a></td>
<td>5</td>
<td>4</td>
<td>2</td>
<td>11</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36120">Серафим Шибанов</a></td>
<td>4</td>
<td>4</td>
<td>3</td>
<td>11</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/80113">Умбет Ержан</a></td>
<td>3</td>
<td>5</td>
<td>3</td>
<td>11</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/70750">Денис Галиакберов</a></td>
<td>6</td>
<td>1</td>
<td>3</td>
<td>10</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/58995">Игорь Пятов</a></td>
<td>5</td>
<td>0</td>
<td>5</td>
<td>10</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51734">Дархан Медеуов</a></td>
<td>3</td>
<td>4</td>
<td>3</td>
<td>10</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/56618">Александр Орлов</a></td>
<td>2</td>
<td>5</td>
<td>3</td>
<td>10</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71811">Мария Гальцер</a></td>
<td>2</td>
<td>5</td>
<td>3</td>
<td>10</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/59005">Александр Дубровский</a></td>
<td>2</td>
<td>3</td>
<td>5</td>
<td>10</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/101392">Антон Иванов</a></td>
<td>1</td>
<td>5</td>
<td>4</td>
<td>10</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51716">Аскар Мулькубаев</a></td>
<td>4</td>
<td>4</td>
<td>1</td>
<td>9</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19915">Александр Марков</a></td>
<td>4</td>
<td>3</td>
<td>2</td>
<td>9</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/74382">Михаил Новосёлов</a></td>
<td>4</td>
<td>3</td>
<td>2</td>
<td>9</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71846">Ерден Шегир</a></td>
<td>2</td>
<td>4</td>
<td>3</td>
<td>9</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/66296">Сергей Чистяков</a></td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>9</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71752">Марат Калдыбаев</a></td>
<td>1</td>
<td>5</td>
<td>3</td>
<td>9</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54160">Станислав Конев</a></td>
<td>4</td>
<td>2</td>
<td>2</td>
<td>8</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/53984">Талгат Шагамбаев</a></td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>8</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54035">Дамир Жадиков</a></td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>7</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>1</td>
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
<td><a href="https://rating.chgk.info/player/116146">Канат Куанбаев</a></td>
<td>3</td>
<td>2</td>
<td>2</td>
<td>7</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51773">Олжас Усипбаев</a></td>
<td>2</td>
<td>4</td>
<td>1</td>
<td>7</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51736">Кайрат Имашев</a></td>
<td>2</td>
<td>3</td>
<td>2</td>
<td>7</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/57328">Руслан Шуканов</a></td>
<td>2</td>
<td>1</td>
<td>4</td>
<td>7</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/62768">Ерлан Кузбаков</a></td>
<td>2</td>
<td>3</td>
<td>1</td>
<td>6</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13535">Руслан Каримов</a></td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>6</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54033">Ернар Ашимов</a></td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/130944">Темирлан Сафаргалиев</a></td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>6</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/53983">Серикжан Ниязов</a></td>
<td>2</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71845">Олег Цыганов</a></td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>5</td>
<td>0</td>
<td>2</td>
<td>1</td>
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
<td><a href="https://rating.chgk.info/player/78135">Виктория Заричанская</a></td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>5</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/176076">Ерлан Мухамеджанов</a></td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>5</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/59510">Дана Рысбекова</a></td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/131908">Иван Киселёв</a></td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>1</td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5244">Алексей Вашкевич</a></td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/39431">Анастасия Белова</a></td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>1</td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71430">Рустем Садыков</a></td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>4</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51758">Диас Казбекулы</a></td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
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
<td><a href="https://rating.chgk.info/player/62760">Абылай Жексембай</a></td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/195360">Никита Ковалёв</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51807">Алтынгуль Шуканова</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/91388">Эльдар Кощегулов</a></td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/100347">Дмитрий Ларионов</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/86775">Рузель Халиуллин</a></td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
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
<td><a href="https://rating.chgk.info/player/61910">Берликан Туспаев</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51757">Дмитрий Абдразаков</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/40840">Денис Макаров</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>0</td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71297">Алеся Ткаченко</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18394">Игорь Линцов</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
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
<td><a href="https://rating.chgk.info/player/123495">Сакен Истамкулов</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
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
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/116143">Айбек Мендигалиев</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/323">Заур Агаев</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51761">Алибек Дильтаев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29669">Ася Смирнова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51717">Ержан Джапаров</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/59150">Адиль Тажин</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
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
<td><a href="https://rating.chgk.info/player/182251">Айнур Мубарова</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/82965">Кайрат Тубалыков</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/79459">Мария Валяева</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31056">Тимур Сыздыков</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/84122">Алиса Пикулина</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/133025">Елдос Жиембаев</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/56364">Кайыргали Беккали</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/85019">Любовь Василец</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
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
<td><a href="https://rating.chgk.info/player/128270">Михаил Шурыгин</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1380094">Роман Павлов</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/46409">Евгений Василец</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
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
<td><a href="https://rating.chgk.info/player/53982">Бекзат Губашев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/57318">Денис Шевелёв</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13196">Евгений Калюков</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/57327">Константин Середнюк</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27912">Рустамхужа Саид-Аминов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51721">Сункар Шагамбаев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11449">Виталий Заря</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/125187">Дмитрий Качурин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51745">Дмитрий Клепиков</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30660">Юлия Заря</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/42901">Юрий Воропаев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/62763">Бекарыс Нурумбетов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/97435">Джияна Ичигеева</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51759">Ильяс Жармуханбетов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/142090">Абдугани Сафи</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/173634">Адлет Раимбеков</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/69812">Анастасия Алёхина</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/136065">Андрей Дудкин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/172928">Арман Асангалиев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/82963">Арнур Аманов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/185163">Артур Могулевский</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51800">Асылжан Акынова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/193713">Бахытжан Иминов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23548">Вадим Орлов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/79483">Далер Аманбаев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71429">Данияр Жумадилов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/257824">Дина Алеева</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/185159">Дмитрий Ефремов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51746">Евгений Вуколов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/185160">Камилла Райхель</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/95878">Надира Шокетаева</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/200306">Олег Рубанов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/55880">Полина Новик</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54309">Расул Тохниязов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/185161">Салтанат Ефремова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/179997">Сардар Садыков</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/116555">Тарим Асимов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4394">Тимур Букетов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/62766">Азат Дарменов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36940">Александр Эпп</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18477">Алексей Литвинас</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/245811">Алексей Шкрабов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54199">Алмас Серикулы</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/59509">Анвар Азимов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/114281">Ахан Жуматаев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/249561">Елена Доморецкая</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/190200">Марат Амиров</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15430">Марат Конкаков</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/249285">Меруерт Акканова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30370">Павел Старовик</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/59508">Акбота Имашева</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/182637">Алексей Лапин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/152275">Алым Надыров</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/194381">Борис Мазец</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/55878">Виталий Фомин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/133298">Дархан Молдашев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/238875">Дмитрий Сапига</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51720">Евгений Мумджян</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/82964">Никита Синьков</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/87797">Олег Додонов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/224068">Ольга Семенчук</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/59544">Ренат Арифуллин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/152276">Рустам Калиев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/97705">Санжар Султанов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/152277">Тимофей Стёпкин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-kvrm"></div>

<a id="game-kvrm"></a><a id="kvrm_contents" name="kvrm_contents"></a>

- [XIV чемпионат Казахстана по КВРМ (2026)](#kvrm_2026)
- [XIII чемпионат Казахстана по КВРМ (2025)](#kvrm_2025)
- [XII чемпионат Казахстана по КВРМ (2024)](#kvrm_2024)
- [XI чемпионат Казахстана по КВРМ (2023)](#kvrm_2023)
- [X чемпионат Казахстана по КВРМ (2022)](#kvrm_2022)
- [IX чемпионат Казахстана по спортивному ЧГК (2019)](#chgk_2019)
- [VIII чемпионат Казахстана по спортивному ЧГК (2018)](#chgk_2018)
- [VII чемпионат Казахстана по спортивному ЧГК (2017)](#chgk_2017)
- [VI чемпионат Казахстана по спортивному ЧГК (2016)](#chgk_2016)
- [V чемпионат Казахстана по спортивному ЧГК (2015)](#chgk_2015)
- [IV чемпионат Казахстана по спортивному ЧГК (2014)](#chgk_2014)
- [III чемпионат Казахстана по спортивному ЧГК (2013)](#chgk_2013)
- [II чемпионат Казахстана по спортивному ЧГК (2012)](#chgk_2012)
- [I чемпионат Казахстана по спортивному ЧГК (2011)](#chgk_2011)


**XIV чемпионат Казахстана по командной викторине с раундами по минуте** прошёл 27–28 июня 2026 года в Алматы. <a name="kvrm_2026"></a>

Победитель: **[«Интеллект-экипаж» (Алматы)](https://rating.chgk.info/teams/93605)**
- Иван Киселёв
- Валерий Есаулков
- Михаил Новосёлов
- Дамир Жадиков
- Анвар Мухаметкалиев
- Александр Марков

Второе место заняла команда [«Осторожно, надвигается кайфун»](https://rating.chgk.info/teams/89600) (Астана), третье — [«Элизабет Пэрриш»](https://rating.chgk.info/teams/93518) (Алматы).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/13686). Фотографии с турнира можно посмотреть по [этой ссылке](https://drive.google.com/drive/folders/1bt02DmEyO7HaKnIDEuuLxjZ8NVneUI4a?usp=sharing). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chkiixiii/125) и [здесь](https://t.me/chgknews/1501).


*[К оглавлению](#kvrm_contents)*

---

**XIII чемпионат Казахстана по командной викторине с раундами по минуте** прошёл 14–15 июня 2025 года в Алматы. <a name="kvrm_2025"></a>

Победитель: **[«Элизабет Пэрриш» (Алматы)](https://rating.chgk.info/teams/93518)**
- Умбет Ержан
- Ерден Шегир
- Муслима Карабалаева
- Данияр Алпысбай
- Дария Жылкыбаева
- Алексей Вашкевич

Второе место заняла команда [«Интеллект-экипаж»](https://rating.chgk.info/teams/93605) (Алматы), третье — [«Осторожно, надвигается кайфун»](https://rating.chgk.info/teams/89600) (Астана).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12094), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/6452). Фотографии с турнира можно посмотреть по [этой ссылке](https://drive.google.com/drive/folders/1Gwsd4MRNj3k5upsmrYpv4sr5zjB8YryR). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chkiixiii/79) и [здесь](https://t.me/chgknews/1178).


*[К оглавлению](#kvrm_contents)*

---

**XII чемпионат Казахстана по командной викторине с раундами по минуте** прошёл 1–2 июня 2024 года в Астане. <a name="kvrm_2024"></a>

Победитель: **[«Элизабет Пэрриш» (Алматы)](https://rating.chgk.info/teams/37797)**
- Сакен Истамкулов
- Умбет Ержан
- Муслима Карабалаева
- Абылай Жексембай
- Данияр Алпысбай
- Дария Жылкыбаева

Второе место заняла команда [«Резко континентальные»](https://rating.chgk.info/teams/42100) (Астана), третье — [«Рецессивный доминант»](https://rating.chgk.info/teams/91036) (Астана).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/10723), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/6441). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chgkastana) и [здесь](https://t.me/chgknews/858).


*[К оглавлению](#kvrm_contents)*

---

**XI чемпионат Казахстана по командной викторине с раундами по минуте** прошёл 17–18 июня 2023 года в Алматы. <a name="kvrm_2023"></a>

Победитель: **[«Ангел в тюбетейке» (Астана)](https://rating.chgk.info/teams/89600)**
- Рузель Халиуллин
- Денис Галиакберов
- Азат Тургунов
- Мольдер Рубанова
- Антон Горский
- Серафим Шибанов
- Бауржан Бектемиров

Второе место заняла команда [«Brain Art»](https://rating.chgk.info/teams/27684) (Алматы), третье — [«Простые работяги»](https://rating.chgk.info/teams/88108) (Алматы).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/9008), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/6442). Фотографии с турнира можно посмотреть по [этой ссылке](https://disk.yandex.kz/d/c0EJO7xdM-giZQ).


*[К оглавлению](#kvrm_contents)*

---

**X чемпионат Казахстана по командной викторине с раундами по минуте** прошёл 8–9 октября 2022 года в Алматы. <a name="kvrm_2022"></a>

Победитель: **[«Приятные люди» (Астана)](https://rating.chgk.info/teams/76272)**
- Муслима Карабалаева
- Данияр Алпысбай
- Антон Горский
- Дария Жылкыбаева
- Кайрат Имашев
- Бауржан Бектемиров

Второе место заняла команда [«Простые работяги»](https://rating.chgk.info/teams/88108) (Алматы), третье — [«Brain Art»](https://rating.chgk.info/teams/27684) (Алматы).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/8555), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/5403).


*[К оглавлению](#kvrm_contents)*

---

**IX чемпионат Казахстана по спортивному «Что? Где? Когда?»** прошёл 6–7 апреля 2019 года в Алматы. <a name="chgk_2019"></a>

Победитель: **[«Бедлам» (Астана)](https://rating.chgk.info/teams/41492)**
- Руслан Жолсеитов
- Азат Тургунов
- Антон Горский
- Дария Жылкыбаева
- Дархан Медеуов
- Герман Смирнов
- Бауржан Бектемиров

Второе место заняла команда [«Эрудит»](https://rating.chgk.info/teams/37797) (Алматы), третье — [«Quantum»](https://rating.chgk.info/teams/49225) (Алматы).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5487).


*[К оглавлению](#kvrm_contents)*

---

**VIII чемпионат Казахстана по спортивному «Что? Где? Когда?»** прошёл 16–17 июня 2018 года в Актау. <a name="chgk_2018"></a>

Победитель: **[«Бедлам» (Астана)](https://rating.chgk.info/teams/41492)**
- Руслан Жолсеитов
- Муслима Карабалаева
- Берликан Туспаев
- Дария Жылкыбаева
- Герман Смирнов
- Бауржан Бектемиров

Второе место заняла команда [«И никого не стало»](https://rating.chgk.info/teams/65159) (Алматы), третье — [«Резко континентальные»](https://rating.chgk.info/teams/42100) (Астана).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5049).


*[К оглавлению](#kvrm_contents)*

---

**VII чемпионат Казахстана по спортивному «Что? Где? Когда?»** прошёл 25–26 марта 2017 года в Астане. <a name="chgk_2017"></a>

Победитель: **[«Бедлам» (Астана)](https://rating.chgk.info/teams/41492)**
- Руслан Жолсеитов
- Муслима Карабалаева
- Азат Тургунов
- Руслан Шуканов
- Антон Горский
- Дархан Медеуов

Второе место заняла команда [«Эрудит»](https://rating.chgk.info/teams/37797) (Алматы), третье — [«Команда Игоря Пятова»](https://rating.chgk.info/teams/49225) (Алматы).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4235).


*[К оглавлению](#kvrm_contents)*

---

**VI чемпионат Казахстана по спортивному «Что? Где? Когда?»** прошёл 23–24 апреля 2016 года в Астане. <a name="chgk_2016"></a>

Победитель: **[«Команда Игоря Пятова» (Алматы)](https://rating.chgk.info/teams/49225)**
- Сергей Чистяков
- Игорь Пятов
- Дария Жылкыбаева
- Валерий Володин
- Анвар Мухаметкалиев
- Герман Смирнов

Второе место заняла команда [«Бедлам»](https://rating.chgk.info/teams/41492) (Астана), третье — [«Brain Art»](https://rating.chgk.info/teams/27684) (Алматы).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3790).


*[К оглавлению](#kvrm_contents)*

---

**V чемпионат Казахстана по спортивному «Что? Где? Когда?»** прошёл 9–10 мая 2015 года в Астане. <a name="chgk_2015"></a>

Победитель: **[«Резко континентальные» (Астана)](https://rating.chgk.info/teams/42100)**
- Виктория Заричанская
- Мария Гальцер
- Мария Сеилова
- Эльдар Бейсимбеков
- Марат Калдыбаев
- Александр Орлов
- Фарит Алиби

Второе место заняла команда [«Бедлам»](https://rating.chgk.info/teams/41492) (Астана), третье — [«Brain Art»](https://rating.chgk.info/teams/27684) (Алматы).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3291).


*[К оглавлению](#kvrm_contents)*

---

**IV чемпионат Казахстана по спортивному «Что? Где? Когда?»** прошёл 28–29 марта 2014 года в Алматы. <a name="chgk_2014"></a>

Победитель: **[«Альфа» (Алматы)](https://rating.chgk.info/teams/27683)**
- Тимур Шайткалиев
- Станислав Конев
- Валерий Володин
- Валерия Вознесенская
- Аскар Мулькубаев
- Анвар Мухаметкалиев
- Герман Смирнов

Второе место заняла команда [«Бедлам»](https://rating.chgk.info/teams/41492) (Астана), третье — [«Brain Art»](https://rating.chgk.info/teams/27684) (Алматы).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2848).


*[К оглавлению](#kvrm_contents)*

---

**III чемпионат Казахстана по спортивному «Что? Где? Когда?»** прошёл 31 мая–1 июня 2013 года в Алматы. <a name="chgk_2013"></a>

Победитель: **[«Альфа» (Алматы)](https://rating.chgk.info/teams/27683)**
- Тимур Шайткалиев
- Станислав Конев
- Валерий Володин
- Валерия Вознесенская
- Аскар Мулькубаев
- Анвар Мухаметкалиев
- Герман Смирнов

Второе место заняла команда [«Бедлам»](https://rating.chgk.info/teams/41492) (Астана), третье — [«Эрудит»](https://rating.chgk.info/teams/37797) (Алматы).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2414).


*[К оглавлению](#kvrm_contents)*

---

**II чемпионат Казахстана по спортивному «Что? Где? Когда?»** прошёл 17–18 февраля 2012 года в Астане. <a name="chgk_2012"></a>

Победитель: **[«Brain Art» (Алматы)](https://rating.chgk.info/teams/27684)**
- Талгат Шагамбаев
- Серикжан Ниязов
- Бекзат Губашев
- Антон Горский
- Чингиз Жылкыбаев
- Сункар Шагамбаев

Второе место заняла команда [«Glory»](https://rating.chgk.info/teams/37654) (Алматы), третье — [«Альфа»](https://rating.chgk.info/teams/27683) (Алматы).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2015), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3151).


*[К оглавлению](#kvrm_contents)*

---

**I чемпионат Казахстана по спортивному «Что? Где? Когда?»** прошёл 17–18 июня 2011 года в Актау. <a name="chgk_2011"></a>

Победитель: **[«Анкор» (Актау)](https://rating.chgk.info/teams/39765)**
- Руслан Шуканов
- Константин Середнюк
- Денис Шевелёв
- Рустамхужа Саид-Аминов
- Игорь Линцов
- Евгений Калюков

Второе место заняла команда [«Альфа»](https://rating.chgk.info/teams/27683) (Алматы), третье — [«Страх и ненависть в Майкудуке»](https://rating.chgk.info/teams/7570) (Караганда).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1874), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3520).


*[К оглавлению](#kvrm_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-brain"></div>

<a id="game-brain"></a><a id="brain_contents" name="brain_contents"></a>

- [X чемпионат Казахстана по БР (2026)](#brain_2026)
- [IX чемпионат Казахстана по БР (2024)](#brain_2024)
- [VIII чемпионат Казахстана по БР (2023)](#brain_2023)
- [VII чемпионат Казахстана по БР (2022)](#brain_2022)
- [VI чемпионат Казахстана по БР (2019)](#brain_2019)
- [V чемпионат Казахстана по БР (2018)](#brain_2018)
- [IV чемпионат Казахстана по БР (2017)](#brain_2017)
- [III чемпионат Казахстана по БР (2016)](#brain_2016)
- [II чемпионат Казахстана по БР (2015)](#brain_2015)
- [I чемпионат Казахстана по БР (2014)](#brain_2014)


**X чемпионат Казахстана по брейн-рингу** прошёл 27–28 июня 2026 года в Алматы. <a name="brain_2026"></a>

Победитель: **[«Осторожно, надвигается кайфун» (Астана)](https://rating.chgk.info/teams/89600)**
- Денис Галиакберов
- Азат Тургунов
- Мольдер Рубанова
- Антон Горский
- Анастасия Белова
- Серафим Шибанов
- Бауржан Бектемиров

Второе место заняла команда [«Резко континентальные»](https://rating.chgk.info/teams/42100) (Астана), третье — [«Интеллект-экипаж»](https://rating.chgk.info/teams/93605) (Алматы).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1W6crPMcXTU6TyXW66QQxjfgasK3cs2gQYwX9LMC4qYE/edit?gid=727059521#gid=727059521). Фотографии с турнира можно посмотреть по [этой ссылке](https://drive.google.com/drive/folders/1bt02DmEyO7HaKnIDEuuLxjZ8NVneUI4a?usp=sharing). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chkiixiii/125) и [здесь](https://t.me/chgknews/1501).


*[К оглавлению](#brain_contents)*

---

**IX чемпионат Казахстана по брейн-рингу** прошёл 1–2 июня 2024 года в Астане. <a name="brain_2024"></a>

Победитель: **[«Интеллект-экипаж» (Алматы)](https://rating.chgk.info/teams/93605)**
- Дамир Жадиков
- Анвар Мухаметкалиев
- Александр Марков
- Валерий Есаулков
- Михаил Новосёлов
- Иван Киселёв

Второе место заняла команда [«Резко континентальные»](https://rating.chgk.info/teams/42100) (Астана), третье — [«Brain Art»](https://rating.chgk.info/teams/27684) (Алматы).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1k7HtGU4FYnnC_symgVwpsjxynFt6KjYaiaDF4XIYPqg/edit#gid=1085381949). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chgkastana) и [здесь](https://t.me/chgknews/858).


*[К оглавлению](#brain_contents)*

---

**VIII чемпионат Казахстана по брейн-рингу** прошёл 17–18 июня 2023 года в Алматы. <a name="brain_2023"></a>

Победитель: **[«No Буратинос» (Астана)](https://rating.chgk.info/teams/27429)**
- Алексей Вашкевич
- Александр Орлов
- Дмитрий Качурин
- Юлия Заря
- Виталий Заря
- Юрий Воропаев

Второе место заняла команда [«Brain Art»](https://rating.chgk.info/teams/27684) (Алматы), третье — [«Ангел в тюбетейке»](https://rating.chgk.info/teams/89600) (Астана).


*[К оглавлению](#brain_contents)*

---

**VII чемпионат Казахстана по брейн-рингу** прошёл 8–9 октября 2022 года в Алматы. <a name="brain_2022"></a>

Победитель: **[«Простые работяги» (Алматы)](https://rating.chgk.info/teams/88108)**
- Валерий Есаулков
- Михаил Новосёлов
- Азат Тургунов
- Мольдер Рубанова
- Валерий Володин
- Анвар Мухаметкалиев
- Александр Марков

Второе место заняла команда [«Приятные люди»](https://rating.chgk.info/teams/76272) (Астана), третье — [«Резко континентальные»](https://rating.chgk.info/teams/42100) (Астана).


*[К оглавлению](#brain_contents)*

---

**VI чемпионат Казахстана по брейн-рингу** прошёл 6–7 апреля 2019 года в Алматы. <a name="brain_2019"></a>

Победитель: **[«Brain Art» (Алматы)](https://rating.chgk.info/teams/27684)**
- Чингиз Жылкыбаев
- Тимур Шайткалиев
- Александр Дубровский
- Дана Рысбекова
- Дмитрий Абдразаков
- Дмитрий Клепиков

Второе место заняла команда [«Басенджи»](https://rating.chgk.info/teams/68172) (Алматы), третье — [«Der Рефрижератор»](https://rating.chgk.info/teams/42364) (Караганда).


*[К оглавлению](#brain_contents)*

---

**V чемпионат Казахстана по брейн-рингу** прошёл 16–17 июня 2018 года в Актау. <a name="brain_2018"></a>

Победитель: **[«И никого не стало» (Алматы)](https://rating.chgk.info/teams/65159)**
- Валерий Есаулков
- Канат Куанбаев
- Дмитрий Ларионов
- Дана Рысбекова
- Валерий Володин
- Анвар Мухаметкалиев

Второе место заняла команда [«Каспий»](https://rating.chgk.info/teams/38145) (Актау), третье — [«Эрудит»](https://rating.chgk.info/teams/37797) (Алматы).


*[К оглавлению](#brain_contents)*

---

**IV чемпионат Казахстана по брейн-рингу** прошёл 25–26 марта 2017 года в Астане. <a name="brain_2017"></a>

Победитель: **[«Эрудит» (Алматы)](https://rating.chgk.info/teams/37797)**
- Умбет Ержан
- Ерден Шегир
- Олег Цыганов
- Ерлан Кузбаков
- Данияр Алпысбай
- Руслан Каримов

Второе место заняла команда [«Резко континентальные»](https://rating.chgk.info/teams/42100) (Астана), третье — [«Бедлам»](https://rating.chgk.info/teams/41492) (Астана).


*[К оглавлению](#brain_contents)*

---

**III чемпионат Казахстана по брейн-рингу** прошёл 23–24 апреля 2016 года в Астане. <a name="brain_2016"></a>

Победитель: **[«Бедлам» (Астана)](https://rating.chgk.info/teams/41492)**
- Руслан Жолсеитов
- Муслима Карабалаева
- Азат Тургунов
- Антон Горский
- Дархан Медеуов
- Валерия Вознесенская

Второе место заняла команда [«Крылья Гавриила»](https://rating.chgk.info/teams/27685) (Алматы), третье — [«Резко континентальные»](https://rating.chgk.info/teams/42100) (Астана).


*[К оглавлению](#brain_contents)*

---

**II чемпионат Казахстана по брейн-рингу** прошёл 9–10 мая 2015 года в Астане. <a name="brain_2015"></a>

Победитель: **[«Brain Art» (Алматы)](https://rating.chgk.info/teams/27684)**
- Тимур Шайткалиев
- Александр Дубровский
- Мольдер Рубанова
- Ернар Ашимов
- Талгат Шагамбаев
- Чингиз Жылкыбаев

Второе место заняла команда [«Резко континентальные»](https://rating.chgk.info/teams/42100) (Астана), третье — [«Ничоси»](https://rating.chgk.info/teams/49225) (Алматы).


*[К оглавлению](#brain_contents)*

---

**I чемпионат Казахстана по брейн-рингу** прошёл 28–29 марта 2014 года в Алматы. <a name="brain_2014"></a>

Победитель: **[«Альфа» (Алматы)](https://rating.chgk.info/teams/27683)**
- Тимур Шайткалиев
- Станислав Конев
- Валерий Володин
- Валерия Вознесенская
- Аскар Мулькубаев
- Анвар Мухаметкалиев
- Герман Смирнов

Второе место заняла команда [«Эрудит»](https://rating.chgk.info/teams/37797) (Алматы), третье — [«Крылья Гавриила»](https://rating.chgk.info/teams/27685) (Алматы).


*[К оглавлению](#brain_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-hamsa"></div>

<a id="game-hamsa"></a><a id="hamsa_contents" name="hamsa_contents"></a>

- [XI чемпионат Казахстана по «Хамсе» (2025)](#hamsa_2025)
- [X чемпионат Казахстана по «Хамсе» (2024)](#hamsa_2024)
- [IX чемпионат Казахстана по «Хамсе» (2023)](#hamsa_2023)
- [VIII чемпионат Казахстана по «Хамсе» (2022)](#hamsa_2022)
- [VII чемпионат Казахстана по «Хамсе» (2019)](#hamsa_2019)
- [VI чемпионат Казахстана по «Хамсе» (2018)](#hamsa_2018)
- [V чемпионат Казахстана по «Хамсе» (2017)](#hamsa_2017)
- [IV чемпионат Казахстана по «Хамсе» (2016)](#hamsa_2016)
- [III чемпионат Казахстана по «Хамсе» (2015)](#hamsa_2015)
- [II чемпионат Казахстана по «Хамсе» (2014)](#hamsa_2014)
- [I чемпионат Казахстана по «Хамсе» (2013)](#hamsa_2013)


**XI чемпионат Казахстана по «Хамсе»** прошёл 14–15 июня 2025 года в Алматы. <a name="hamsa_2025"></a>

Победитель: **[«Осторожно, надвигается кайфун» (Астана)](https://rating.chgk.info/teams/89600)**
- Денис Галиакберов
- Азат Тургунов
- Мольдер Рубанова
- Антон Горский
- Анастасия Белова
- Серафим Шибанов
- Бауржан Бектемиров

Второе место заняла команда [«Первый номер драфта»](https://rating.chgk.info/teams/91998) (Астана), третье — [«Интеллект-экипаж»](https://rating.chgk.info/teams/93605) (Алматы).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/12ui1bKV_u2JBfGmfkJ79b7eztJXXiBdnUy8d16FJ3ws/edit?gid=373395725#gid=373395725). Фотографии с турнира можно посмотреть по [этой ссылке](https://drive.google.com/drive/folders/1Gwsd4MRNj3k5upsmrYpv4sr5zjB8YryR). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chkiixiii/79) и [здесь](https://t.me/chgknews/1178).


*[К оглавлению](#hamsa_contents)*

---

**X чемпионат Казахстана по «Хамсе»** прошёл 1–2 июня 2024 года в Астане. <a name="hamsa_2024"></a>

Победитель: **[«Резко континентальные» (Астана)](https://rating.chgk.info/teams/42100)**
- Антон Иванов
- Мария Гальцер
- Мария Сеилова
- Эльдар Бейсимбеков
- Фарит Алиби
- Диас Казбекулы

Второе место заняла команда [«Эрудит»](https://rating.chgk.info/teams/37797) (Алматы), третье — [«Ангел в тюбетейке»](https://rating.chgk.info/teams/89600) (Астана).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1k7HtGU4FYnnC_symgVwpsjxynFt6KjYaiaDF4XIYPqg/edit#gid=900255789). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chgkastana) и [здесь](https://t.me/chgknews/858).


*[К оглавлению](#hamsa_contents)*

---

**IX чемпионат Казахстана по «Хамсе»** прошёл 17–18 июня 2023 года в Алматы. <a name="hamsa_2023"></a>

Победитель: **[«Ангел в тюбетейке» (Астана)](https://rating.chgk.info/teams/89600)**
- Рузель Халиуллин
- Денис Галиакберов
- Азат Тургунов
- Мольдер Рубанова
- Антон Горский
- Серафим Шибанов
- Бауржан Бектемиров

Второе место заняла команда [«Простые работяги»](https://rating.chgk.info/teams/88108) (Алматы), третье — [«Вжух»](https://rating.chgk.info/teams/59835) (Алматы).


*[К оглавлению](#hamsa_contents)*

---

**VIII чемпионат Казахстана по «Хамсе»** прошёл 8–9 октября 2022 года в Алматы. <a name="hamsa_2022"></a>

Победитель: **[«Простые работяги» (Алматы)](https://rating.chgk.info/teams/88108)**
- Валерий Есаулков
- Михаил Новосёлов
- Азат Тургунов
- Мольдер Рубанова
- Валерий Володин
- Анвар Мухаметкалиев
- Александр Марков

Второе место заняла команда [«Brain Art»](https://rating.chgk.info/teams/27684) (Алматы), третье — [«Приятные люди»](https://rating.chgk.info/teams/76272) (Астана).


*[К оглавлению](#hamsa_contents)*

---

**VII чемпионат Казахстана по «Хамсе»** прошёл 6–7 апреля 2019 года в Алматы. <a name="hamsa_2019"></a>

Победитель: **[«Quantum» (Алматы)](https://rating.chgk.info/teams/49225)**
- Валерий Есаулков
- Канат Куанбаев
- Айбек Мендигалиев
- Игорь Пятов
- Мольдер Рубанова
- Валерий Володин
- Заур Агаев
- Анвар Мухаметкалиев

Второе место заняла команда [«Бедлам»](https://rating.chgk.info/teams/41492) (Астана), третье — [«Резко континентальные»](https://rating.chgk.info/teams/42100) (Астана).


*[К оглавлению](#hamsa_contents)*

---

**VI чемпионат Казахстана по «Хамсе»** прошёл 16–17 июня 2018 года в Актау. <a name="hamsa_2018"></a>

Победитель: **[«И никого не стало» (Алматы)](https://rating.chgk.info/teams/65159)**
- Валерий Есаулков
- Канат Куанбаев
- Дмитрий Ларионов
- Дана Рысбекова
- Валерий Володин
- Анвар Мухаметкалиев

Второе место заняла команда [«Резко континентальные»](https://rating.chgk.info/teams/42100) (Астана), третье — [«Каспий»](https://rating.chgk.info/teams/38145) (Актау).


*[К оглавлению](#hamsa_contents)*

---

**V чемпионат Казахстана по «Хамсе»** прошёл 25–26 марта 2017 года в Астане. <a name="hamsa_2017"></a>

Победитель: **[«Ничоси» (Алматы)](https://rating.chgk.info/teams/49225)**
- Игорь Пятов
- Ибрагимова
- Кайрат Имашев
- Валерий Володин
- Анвар Мухаметкалиев
- Герман Смирнов

Второе место заняла команда [«Brain Art»](https://rating.chgk.info/teams/27684) (Алматы), третье — [«Тропик Рака»](https://rating.chgk.info/teams/45560) (Астана).


*[К оглавлению](#hamsa_contents)*

---

**IV чемпионат Казахстана по «Хамсе»** прошёл 23–24 апреля 2016 года в Астане. <a name="hamsa_2016"></a>

Победитель: **[«Ничоси» (Алматы)](https://rating.chgk.info/teams/49225)**
- Сергей Чистяков
- Игорь Пятов
- Дария Жылкыбаева
- Валерий Володин
- Анвар Мухаметкалиев
- Герман Смирнов

Второе место заняла команда [«Крылья Гавриила»](https://rating.chgk.info/teams/27685) (Алматы), третье — [«Бедлам»](https://rating.chgk.info/teams/41492) (Астана).


*[К оглавлению](#hamsa_contents)*

---

**III чемпионат Казахстана по «Хамсе»** прошёл 9–10 мая 2015 года в Астане. <a name="hamsa_2015"></a>

Победитель: **[«Ничоси» (Алматы)](https://rating.chgk.info/teams/49225)**
- Анвар Мухаметкалиев
- Герман Смирнов
- Олжас Усипбаев
- Дария Жылкыбаева
- Игорь Пятов
- Серикжан Ниязов
- Валерий Володин

Второе место разделили команды [«ДНК»](https://rating.chgk.info/teams/45560) (Астана), [«Бедлам»](https://rating.chgk.info/teams/41492) (Астана) и [«Крылья Гавриила»](https://rating.chgk.info/teams/27685) (Алматы).


*[К оглавлению](#hamsa_contents)*

---

**II чемпионат Казахстана по «Хамсе»** прошёл 28–29 марта 2014 года в Алматы. <a name="hamsa_2014"></a>

Победитель: **[«Альфа» (Алматы)](https://rating.chgk.info/teams/27683)**
- Тимур Шайткалиев
- Станислав Конев
- Валерий Володин
- Валерия Вознесенская
- Аскар Мулькубаев
- Анвар Мухаметкалиев
- Герман Смирнов

Второе место заняла команда [«Север Помнит»](https://rating.chgk.info/teams/41492) (Астана), третье — [«Brain Art»](https://rating.chgk.info/teams/27684) (Алматы).


*[К оглавлению](#hamsa_contents)*

---

**I чемпионат Казахстана по «Хамсе»** прошёл 31 мая–1 июня 2013 года в Алматы. <a name="hamsa_2013"></a>

Победитель: **[«Бедлам» (Астана)](https://rating.chgk.info/teams/41492)**
- Руслан Жолсеитов
- Рустем Садыков
- Азат Тургунов
- Дамир Жадиков
- Антон Горский
- Олжас Усипбаев

Второе место заняла команда [«Poker Face»](https://rating.chgk.info/teams/42320) (Караганда), третье — [«Альфа»](https://rating.chgk.info/teams/27683) (Алматы).


*[К оглавлению](#hamsa_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ssi"></div>

<a id="game-ssi"></a><a id="ssi_contents" name="ssi_contents"></a>

- [XIII чемпионат Казахстана по ССИ (2026)](#ssi_2026)
- [XII чемпионат Казахстана по ССИ (2025)](#ssi_2025)
- [XI чемпионат Казахстана по ССИ (2024)](#ssi_2024)
- [X чемпионат Казахстана по ССИ (2023)](#ssi_2023)
- [IX чемпионат Казахстана по ССИ (2022)](#ssi_2022)
- [VIII чемпионат Казахстана по ССИ (2019)](#ssi_2019)
- [VII чемпионат Казахстана по ССИ (2018)](#ssi_2018)
- [VI чемпионат Казахстана по ССИ (2017)](#ssi_2017)
- [V чемпионат Казахстана по ССИ (2016)](#ssi_2016)
- [IV чемпионат Казахстана по ССИ (2015)](#ssi_2015)
- [III чемпионат Казахстана по ССИ (2014)](#ssi_2014)
- [II чемпионат Казахстана по ССИ (2013)](#ssi_2013)
- [I чемпионат Казахстана по ССИ (2012)](#ssi_2012)


**XIII чемпионат Казахстана по спортивной «Своей игре»** прошёл 27–28 июня 2026 года в Алматы. <a name="ssi_2026"></a>

Победитель: **[Денис Галиакберов](https://rating.chgk.info/player/70750)**

Второе место занял [Серафим Шибанов](https://rating.chgk.info/player/36120), третье — [Эльдар Кощегулов](https://rating.chgk.info/player/91388).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1oQtIDoGK1yt6W-8NZO77MjcBgWRdZgfVYVVQ-FHhFeM/edit?gid=869786358#gid=869786358). Фотографии с турнира можно посмотреть по [этой ссылке](https://drive.google.com/drive/folders/1bt02DmEyO7HaKnIDEuuLxjZ8NVneUI4a?usp=sharing). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chkiixiii/125) и [здесь](https://t.me/chgknews/1501).


*[К оглавлению](#ssi_contents)*

---

**XII чемпионат Казахстана по спортивной «Своей игре»** прошёл 14–15 июня 2025 года в Алматы. <a name="ssi_2025"></a>

Победитель: **[Денис Галиакберов](https://rating.chgk.info/player/70750)**

Второе место занял [Серафим Шибанов](https://rating.chgk.info/player/36120), третье — [Умбет Ержан](https://rating.chgk.info/player/80113).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/111dXYLvLbA0kAibq4_Ma2snfkmfz6fNzuFboA87EPsc/edit?gid=1094989862#gid=1094989862). Фотографии с турнира можно посмотреть по [этой ссылке](https://drive.google.com/drive/folders/1Gwsd4MRNj3k5upsmrYpv4sr5zjB8YryR). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chkiixiii/79) и [здесь](https://t.me/chgknews/1178).


*[К оглавлению](#ssi_contents)*

---

**XI чемпионат Казахстана по спортивной «Своей игре»** прошёл 1–2 июня 2024 года в Астане. <a name="ssi_2024"></a>

Победитель: **[Анвар Мухаметкалиев](https://rating.chgk.info/player/51715)**

Второе место занял [Серафим Шибанов](https://rating.chgk.info/player/36120), третье — [Валерий Есаулков](https://rating.chgk.info/player/122503).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1k7HtGU4FYnnC_symgVwpsjxynFt6KjYaiaDF4XIYPqg/edit#gid=1078057135). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chgkastana) и [здесь](https://t.me/chgknews/858).


*[К оглавлению](#ssi_contents)*

---

**X чемпионат Казахстана по спортивной «Своей игре»** прошёл 17–18 июня 2023 года в Алматы. <a name="ssi_2023"></a>

Победитель: **[Валерий Есаулков](https://rating.chgk.info/player/122503)**

Второе место занял [Антон Горский](https://rating.chgk.info/player/51774), третье — [Азат Тургунов](https://rating.chgk.info/player/59147).


*[К оглавлению](#ssi_contents)*

---

**IX чемпионат Казахстана по спортивной «Своей игре»** прошёл 8–9 октября 2022 года в Алматы. <a name="ssi_2022"></a>

Победитель: **[Валерий Есаулков](https://rating.chgk.info/player/122503)**

Второе место занял [Азат Тургунов](https://rating.chgk.info/player/59147), третье — [Чингиз Жылкыбаев](https://rating.chgk.info/player/51725).


*[К оглавлению](#ssi_contents)*

---

**VIII чемпионат Казахстана по спортивной «Своей игре»** прошёл 6–7 апреля 2019 года в Алматы. <a name="ssi_2019"></a>

Победитель: **[Антон Горский](https://rating.chgk.info/player/51774)**

Второе место занял [Валерий Есаулков](https://rating.chgk.info/player/122503), третье — [Сергей Чистяков](https://rating.chgk.info/player/66296).


*[К оглавлению](#ssi_contents)*

---

**VII чемпионат Казахстана по спортивной «Своей игре»** прошёл 16–17 июня 2018 года в Актау. <a name="ssi_2018"></a>

Победитель: **[Анвар Мухаметкалиев](https://rating.chgk.info/player/51715)**

Второе место занял [Валерий Есаулков](https://rating.chgk.info/player/122503), третье — [Руслан Шуканов](https://rating.chgk.info/player/57328).


*[К оглавлению](#ssi_contents)*

---

**VI чемпионат Казахстана по спортивной «Своей игре»** прошёл 25–26 марта 2017 года в Астане. <a name="ssi_2017"></a>

Победитель: **[Анвар Мухаметкалиев](https://rating.chgk.info/player/51715)**

Второе место занял [Талгат Шагамбаев](https://rating.chgk.info/player/53984), третье — [Бауржан Бектемиров](https://rating.chgk.info/player/2885).


*[К оглавлению](#ssi_contents)*

---

**V чемпионат Казахстана по спортивной «Своей игре»** прошёл 23–24 апреля 2016 года в Астане. <a name="ssi_2016"></a>

Победитель: **[Анвар Мухаметкалиев](https://rating.chgk.info/player/51715)**

Второе место занял [Сергей Чистяков](https://rating.chgk.info/player/66296), третье — [Азат Тургунов](https://rating.chgk.info/player/59147).


*[К оглавлению](#ssi_contents)*

---

**IV чемпионат Казахстана по спортивной «Своей игре»** прошёл 9–10 мая 2015 года в Астане. <a name="ssi_2015"></a>

Победитель: **[Анвар Мухаметкалиев](https://rating.chgk.info/player/51715)**

Второе место занял [Ерлан Кузбаков](https://rating.chgk.info/player/62768), третье — [Игорь Пятов](https://rating.chgk.info/player/58995).


*[К оглавлению](#ssi_contents)*

---

**III чемпионат Казахстана по спортивной «Своей игре»** прошёл 28–29 марта 2014 года в Алматы. <a name="ssi_2014"></a>

Победитель: **[Ерлан Кузбаков](https://rating.chgk.info/player/62768)**

Второе место занял [Анвар Мухаметкалиев](https://rating.chgk.info/player/51715), третье — [Герман Смирнов](https://rating.chgk.info/player/29607).


*[К оглавлению](#ssi_contents)*

---

**II чемпионат Казахстана по спортивной «Своей игре»** прошёл 31 мая–1 июня 2013 года в Алматы. <a name="ssi_2013"></a>

Победитель: **[Анвар Мухаметкалиев](https://rating.chgk.info/player/51715)**

Второе место занял [Станислав Конев](https://rating.chgk.info/player/54160), третье — [Сергей Чистяков](https://rating.chgk.info/player/66296).


*[К оглавлению](#ssi_contents)*

---

**I чемпионат Казахстана по спортивной «Своей игре»** прошёл 17–18 февраля 2012 года в Астане. <a name="ssi_2012"></a>

Победитель: **[Анвар Мухаметкалиев](https://rating.chgk.info/player/51715)**

Второе место занял [Адиль Тажин](https://rating.chgk.info/player/59150), третье — [Игорь Линцов](https://rating.chgk.info/player/18394).


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
<tr><td>2015</td><td>III чемпионат Казахстана по «Хамса»</td><td>неизвестен состав обладателей третьего места.</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
