---
title: Узбекистан
weight: 1
bookToC: false
---

# Узбекистан

Чемпионаты Узбекистана проводятся с 2004 года. Ниже можно увидеть статистику по всем призёрам — как командам, так и игрокам. Также в отдельных вкладках можно найти информацию о чемпионатах страны по той или иной дисциплине. Сейчас не хватает информации о самом первом чемпионате Узбекистана, а также о ряде других турниров. Если вы что-то знаете о призёрах или их составах, напишите, пожалуйста, на почту <chgknews.info@gmail.com>.

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-kvrm" aria-selected="false">Турниры по КВРМ</button><button type="button" role="tab" data-tab="game-ssi" aria-selected="false">Турниры по ССИ</button><button type="button" role="tab" data-tab="missing-data" aria-selected="false">Нет данных</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th>Команда</th><th>Город</th><th>I</th><th>II</th><th>III</th><th>∑</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/2462">Мы</a></td>
<td>Ташкент</td>
<td>3</td>
<td>7</td>
<td>2</td>
<td>12</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/2909">Мистерия</a></td>
<td>Ташкент</td>
<td>6</td>
<td>2</td>
<td>0</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/4864">НМТТ</a></td>
<td>Ташкент</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/4156">7Hz</a></td>
<td>Ташкент</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/5858">DimTeam</a></td>
<td>Ташкент</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/28587">Пахтакор</a></td>
<td>Ташкент</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3449">Veni Vidi Vici</a></td>
<td>Ташкент</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/59318">КАД</a></td>
<td>Ташкент</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/62494">Котовского 26 кв 58</a></td>
<td>Ташкент</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/815">Брюссельские</a></td>
<td>Ташкент</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/4749">ParadoX</a></td>
<td>Навои</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/98988">Комната</a></td>
<td>Ташкент</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3523">Заковат-1</a></td>
<td>Ташкент</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/46377">НЗ</a></td>
<td>сборная</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3687">Dream team</a></td>
<td>Ташкент</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/92163">Императив релоканта</a></td>
<td>Ташкент</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/62644">Ход конём</a></td>
<td>Ташкент</td>
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
<tr><th rowspan="2">Игрок</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">КВРМ</th><th colspan="3" style="text-align:center">ССИ</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/player/18316">Александр Ли</a></td>
<td>4</td>
<td>9</td>
<td>6</td>
<td>19</td>
<td>3</td>
<td>8</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26586">Александр Райков</a></td>
<td>6</td>
<td>10</td>
<td>2</td>
<td>18</td>
<td>5</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>5</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12482">Акрам Икрамов</a></td>
<td>13</td>
<td>4</td>
<td>0</td>
<td>17</td>
<td>10</td>
<td>3</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9240">Абдулазиз Джалилов</a></td>
<td>7</td>
<td>2</td>
<td>7</td>
<td>16</td>
<td>7</td>
<td>2</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7215">Игорь Глущенко</a></td>
<td>8</td>
<td>1</td>
<td>4</td>
<td>13</td>
<td>7</td>
<td>1</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/535">Алексей Акименко</a></td>
<td>6</td>
<td>4</td>
<td>3</td>
<td>13</td>
<td>5</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25981">Галина Прибыткова</a></td>
<td>3</td>
<td>8</td>
<td>2</td>
<td>13</td>
<td>3</td>
<td>7</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/487">Игорь Аипкин</a></td>
<td>7</td>
<td>3</td>
<td>1</td>
<td>11</td>
<td>7</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28654">Артём Семёнов</a></td>
<td>8</td>
<td>2</td>
<td>0</td>
<td>10</td>
<td>6</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35643">Усман Шарифходжаев</a></td>
<td>5</td>
<td>1</td>
<td>4</td>
<td>10</td>
<td>5</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32901">Наиль Фарукшин</a></td>
<td>4</td>
<td>5</td>
<td>1</td>
<td>10</td>
<td>2</td>
<td>5</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2673">Хаким Батыралиев</a></td>
<td>1</td>
<td>5</td>
<td>4</td>
<td>10</td>
<td>1</td>
<td>4</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27912">Рустамхужа Саид-Аминов</a></td>
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
<td><a href="https://rating.chgk.info/player/87499">Наринэ Багдасарян</a></td>
<td>6</td>
<td>2</td>
<td>0</td>
<td>8</td>
<td>6</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4337">Антонина Бударина</a></td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>8</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8986">Наталья Дейнека</a></td>
<td>2</td>
<td>6</td>
<td>0</td>
<td>8</td>
<td>2</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28281">Алексей Саркулов</a></td>
<td>2</td>
<td>1</td>
<td>5</td>
<td>8</td>
<td>2</td>
<td>1</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11220">Аскар Заитов</a></td>
<td>1</td>
<td>4</td>
<td>3</td>
<td>8</td>
<td>1</td>
<td>4</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9801">Егор Дружинин</a></td>
<td>1</td>
<td>4</td>
<td>3</td>
<td>8</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/75099">Сардор Ахмедов</a></td>
<td>4</td>
<td>1</td>
<td>2</td>
<td>7</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35753">Лейла Шахназарова</a></td>
<td>3</td>
<td>0</td>
<td>4</td>
<td>7</td>
<td>3</td>
<td>0</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27827">Дина Сагадиева</a></td>
<td>2</td>
<td>5</td>
<td>0</td>
<td>7</td>
<td>2</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/41902">Валерий Ким</a></td>
<td>2</td>
<td>3</td>
<td>2</td>
<td>7</td>
<td>2</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37142">Азизбек Юсуфов</a></td>
<td>2</td>
<td>1</td>
<td>4</td>
<td>7</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37252">Пётр Яковлев</a></td>
<td>1</td>
<td>5</td>
<td>1</td>
<td>7</td>
<td>1</td>
<td>5</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14394">Владимир Клименко</a></td>
<td>1</td>
<td>1</td>
<td>5</td>
<td>7</td>
<td>1</td>
<td>1</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35180">Алексей Чолоков</a></td>
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
<td><a href="https://rating.chgk.info/player/35750">Георгий Шахназаров</a></td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>6</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19275">Никита Макаренко</a></td>
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
<td><a href="https://rating.chgk.info/player/13782">Тимур Кафиатуллин</a></td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27852">Ян Садковский</a></td>
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
<td><a href="https://rating.chgk.info/player/13674">Алексей Карцевич</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4812">Дмитрий Вагапов</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13196">Евгений Калюков</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/95596">Василий Щедрин</a></td>
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
<td><a href="https://rating.chgk.info/player/152701">Игорь Музыкин</a></td>
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
<td><a href="https://rating.chgk.info/player/6754">Саидакбар Гафуров</a></td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3795">Максим Болонкин</a></td>
<td>0</td>
<td>4</td>
<td>0</td>
<td>4</td>
<td>0</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30537">Игорь Степанян</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37222">Валерия Якимова</a></td>
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
<td><a href="https://rating.chgk.info/player/66802">Галина Никитина</a></td>
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
<td><a href="https://rating.chgk.info/player/30579">Герман Стимбан</a></td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/174012">Павел Корнилов</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/862">Анна Алиева</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32716">Руслан Усманов</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22139">Рустам Надршин</a></td>
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
<td><a href="https://rating.chgk.info/player/34642">Веслав Чеботарь</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19420">Владимир Максимов</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/111198">Ольга Киреева</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/171621">Алексей Грачёв</a></td>
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
<td><a href="https://rating.chgk.info/player/150487">Барно Джалилова</a></td>
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
<td><a href="https://rating.chgk.info/player/26705">Ганишер Рахматуллаев</a></td>
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
<td><a href="https://rating.chgk.info/player/54897">Динара Адылова</a></td>
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
<td><a href="https://rating.chgk.info/player/9299">Отабек Джураев</a></td>
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
<td><a href="https://rating.chgk.info/player/21877">Рустам Мурзаханов</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9808">Александр Друзь</a></td>
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
<td><a href="https://rating.chgk.info/player/32352">Анна Туниянц</a></td>
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
<td><a href="https://rating.chgk.info/player/97435">Джияна Ичигеева</a></td>
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
<td><a href="https://rating.chgk.info/player/110866">Илья Баженов</a></td>
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
<td><a href="https://rating.chgk.info/player/62658">Константин Тен</a></td>
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
<td><a href="https://rating.chgk.info/player/8102">Анаит Григорян</a></td>
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
<td><a href="https://rating.chgk.info/player/29351">Мария Скляревская</a></td>
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
<td><a href="https://rating.chgk.info/player/1239">Михаил Аношкин</a></td>
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
<td><a href="https://rating.chgk.info/player/851">Роман Алиев</a></td>
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
<td><a href="https://rating.chgk.info/player/22886">Рустам Ниязов</a></td>
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
<td><a href="https://rating.chgk.info/player/160062">Абдулазиз Султонов</a></td>
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
<td><a href="https://rating.chgk.info/player/236592">Азиз Ханназаров</a></td>
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
<td><a href="https://rating.chgk.info/player/52744">Асилбек Юсуфов</a></td>
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
<td><a href="https://rating.chgk.info/player/39156">Дмитрий Баранов</a></td>
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
<td><a href="https://rating.chgk.info/player/1826">Жобир Ахмедов</a></td>
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
<td><a href="https://rating.chgk.info/player/22280">Милена Наринян</a></td>
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
<td><a href="https://rating.chgk.info/player/20326">Отабек Махкамов</a></td>
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
<td><a href="https://rating.chgk.info/player/71268">Светлана Корнеева</a></td>
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
<td><a href="https://rating.chgk.info/player/11447">Сослан Зарукаев</a></td>
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
<td><a href="https://rating.chgk.info/player/199137">Умархон Шариф</a></td>
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
<td><a href="https://rating.chgk.info/player/101500">Эльбек Нурмухамедов</a></td>
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
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12021">Агзамходжа Ибрагимов</a></td>
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
<td><a href="https://rating.chgk.info/player/47560">Александр Жудро</a></td>
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
<td><a href="https://rating.chgk.info/player/199770">Алишер Исмаилов</a></td>
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
<td><a href="https://rating.chgk.info/player/24498">Анастасия Пересыпкина</a></td>
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
<td><a href="https://rating.chgk.info/player/1704">Гульнара Асямова</a></td>
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
<td><a href="https://rating.chgk.info/player/6422">Джасурбек Гайбуллаев</a></td>
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
<td><a href="https://rating.chgk.info/player/25121">Дмитрий Плотников</a></td>
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
<td><a href="https://rating.chgk.info/player/25498">Евгений Полюдов</a></td>
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
<td><a href="https://rating.chgk.info/player/22935">Илья Новиков</a></td>
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
<td><a href="https://rating.chgk.info/player/29834">Максим Соболевский</a></td>
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
</tr>
<tr>
<td>Рим Валеев</td>
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
<td><a href="https://rating.chgk.info/player/20956">Рустам Мирзаханов</a></td>
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
<td><a href="https://rating.chgk.info/player/14092">Сергей Киргизов</a></td>
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
<td><a href="https://rating.chgk.info/player/12445">Юрий Идрисов</a></td>
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
<td><a href="https://rating.chgk.info/player/32589">Вадим Улитчев</a></td>
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
<td><a href="https://rating.chgk.info/player/48843">Мурод Хамраев</a></td>
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
<td><a href="https://rating.chgk.info/player/32313">Алла Туктарова</a></td>
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
<td><a href="https://rating.chgk.info/player/15017">Бегзод Козоков</a></td>
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
<td><a href="https://rating.chgk.info/player/10297">Бобур Ёкубов</a></td>
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
<td><a href="https://rating.chgk.info/player/7340">Галина Головань</a></td>
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
<td><a href="https://rating.chgk.info/player/21517">Дмитрий Мордвинцев</a></td>
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
<td><a href="https://rating.chgk.info/player/103">Зайнап Абляева</a></td>
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
<td><a href="https://rating.chgk.info/player/19555">Иван Малов</a></td>
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
<td><a href="https://rating.chgk.info/player/8985">Игорь Дейнека</a></td>
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
<td><a href="https://rating.chgk.info/player/36628">Камила Шукурова</a></td>
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
<td><a href="https://rating.chgk.info/player/239256">Лилия Махмутова</a></td>
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
<td><a href="https://rating.chgk.info/player/106588">Олег Артёменко</a></td>
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
<td><a href="https://rating.chgk.info/player/13321">Рената Канцерова</a></td>
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
<td><a href="https://rating.chgk.info/player/4285">Станислав Брюханов</a></td>
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
<td><a href="https://rating.chgk.info/player/52829">Татьяна Белякова</a></td>
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
<td><a href="https://rating.chgk.info/player/8988">Татьяна Дейнека</a></td>
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
<td><a href="https://rating.chgk.info/player/47565">Тимур Тураев</a></td>
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
<td><a href="https://rating.chgk.info/player/17382">Фуркат Курбанов</a></td>
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
<td><a href="https://rating.chgk.info/player/10602">Азиза Есенбаева</a></td>
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
<td><a href="https://rating.chgk.info/player/200140">Александра Кондращенко</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/143777">Алиса Плотникова</a></td>
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
<td><a href="https://rating.chgk.info/player/14693">Антон Коваленко</a></td>
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
<td><a href="https://rating.chgk.info/player/30152">Артём Сорожкин</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18691">Василий Ломакин</a></td>
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
<td><a href="https://rating.chgk.info/player/7018">Владимир Гиль</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33331">Дарья Фирсова</a></td>
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
<td><a href="https://rating.chgk.info/player/19227">Дмитрий Майгатов</a></td>
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
<td><a href="https://rating.chgk.info/player/94616">Дмитрий Филипский</a></td>
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
<td><a href="https://rating.chgk.info/player/879">Зафар Алимбаев</a></td>
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
<td><a href="https://rating.chgk.info/player/112520">Игорь Стугирёв</a></td>
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
<td><a href="https://rating.chgk.info/player/128044">Ирина Семёнова</a></td>
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
<td><a href="https://rating.chgk.info/player/31447">Ирина Тен</a></td>
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
<td><a href="https://rating.chgk.info/player/68097">Константин Бабанский</a></td>
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
<td><a href="https://rating.chgk.info/player/232449">Константин Григорьев</a></td>
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
<td><a href="https://rating.chgk.info/player/117747">Константин Шалькевич</a></td>
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
<td><a href="https://rating.chgk.info/player/48843">Муроджон Хамраев</a></td>
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
<td><a href="https://rating.chgk.info/player/19478">Олег Малахов</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35461">Руфина Шакурова</a></td>
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
<td><a href="https://rating.chgk.info/player/45763">Сергей Кельнер</a></td>
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
<td><a href="https://rating.chgk.info/player/54899">Станислав Сычевский</a></td>
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
<td><a href="https://rating.chgk.info/player/19544">Татьяна Малкина</a></td>
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
<td><a href="https://rating.chgk.info/player/199896">Филипп Туркин</a></td>
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
<td><a href="https://rating.chgk.info/player/36382">Юрий Шлёнский</a></td>
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


**V чемпионат Узбекистана по «Заковату»** прошёл 30–31 мая 2026 года в Ташкенте. <a name="zakovat_2026"></a>

Победитель: **[«Мистерия» (Ташкент)](https://rating.chgk.info/teams/2909)**
- Павел Корнилов
- Илья Баженов
- Наринэ Багдасарян
- Сардор Ахмедов
- Артём Семёнов
- Акрам Икрамов

Второе место заняла команда [«КАД»](https://rating.chgk.info/teams/59318) (Ташкент), третье — [«Комната»](https://rating.chgk.info/teams/98988) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/13657).


*[К оглавлению](#kvrm_contents)*

---

**IV чемпионат Узбекистана по «Заковату»** прошёл 7–8 июня 2025 года в Ташкенте. <a name="zakovat_2025"></a>

Победитель: **[«Мистерия» (Ташкент)](https://rating.chgk.info/teams/2909)**
- Павел Корнилов
- Наринэ Багдасарян
- Сардор Ахмедов
- Артём Семёнов
- Тимур Кафиатуллин
- Акрам Икрамов

Второе место заняла команда [«Комната»](https://rating.chgk.info/teams/98988) (Ташкент), третье — [«КАД»](https://rating.chgk.info/teams/59318) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12039).


*[К оглавлению](#kvrm_contents)*

---

**III чемпионат Узбекистана по «Заковату»** прошёл 25 мая 2024 года в Ташкенте. <a name="zakovat_2024"></a>

Победитель: **[«Мистерия» (Ташкент)](https://rating.chgk.info/teams/2909)**
- Наринэ Багдасарян
- Сардор Ахмедов
- Артём Семёнов
- Тимур Кафиатуллин
- Акрам Икрамов
- Игорь Аипкин

Второе место заняла команда [«Котовского 26 кв 58»](https://rating.chgk.info/teams/62494) (Ташкент), третье — [«Императив релоканта»](https://rating.chgk.info/teams/92163) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/10780).


*[К оглавлению](#kvrm_contents)*

---

**II чемпионат Узбекистана по «Заковату»** прошёл 14 мая 2023 года в Ташкенте. <a name="zakovat_2023"></a>

Победитель: **[«Котовского 26 кв 58» (Ташкент)](https://rating.chgk.info/teams/62494)**
- Игорь Музыкин
- Джияна Ичигеева
- Наиль Фарукшин
- Дмитрий Плотников
- Егор Дружинин

Второе место заняла команда [«Мистерия»](https://rating.chgk.info/teams/2909) (Ташкент), третье — [«Пахтакор»](https://rating.chgk.info/teams/28587) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/9157).


*[К оглавлению](#kvrm_contents)*

---

**I чемпионат Узбекистана по «Заковату»** прошёл 21 августа 2022 года в Ташкенте. <a name="zakovat_2022"></a>

Победитель: **[«Мистерия» (Ташкент)](https://rating.chgk.info/teams/2909)**
- Алишер Исмаилов
- Наринэ Багдасарян
- Сардор Ахмедов
- Константин Тен
- Артём Семёнов
- Акрам Икрамов
- Игорь Аипкин

Второе место заняла команда [«Пахтакор»](https://rating.chgk.info/teams/28587) (Ташкент), третье — [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/8287).


*[К оглавлению](#kvrm_contents)*

---

**XVI чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 27 октября 2019 года в Ташкенте. <a name="chgk_2019"></a>

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

**XV чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 21–22 апреля 2018 года в Ташкенте. <a name="chgk_2018"></a>

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

**XIV чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 23 апреля 2017 года в Ташкенте. <a name="chgk_2017"></a>

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

**XIII чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 21–22 мая 2016 года в Ташкенте. <a name="chgk_2016"></a>

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

**XII чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 28–29 марта 2015 года в Ташкенте. <a name="chgk_2015"></a>

Победитель: **[«DimTeam» (Ташкент)](https://rating.chgk.info/teams/5858)**
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

**XI чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 22–23 марта 2014 года в Ташкенте. <a name="chgk_2014"></a>

Победитель: **[«DimTeam» (Ташкент)](https://rating.chgk.info/teams/5858)**
- Александр Жудро
- Азизбек Юсуфов
- Усман Шарифходжаев
- Анна Туниянц
- Алексей Карцевич
- Абдулазиз Джалилов
- Игорь Глущенко
- Дмитрий Вагапов

Второе место заняла команда [«НЗ»](https://rating.chgk.info/teams/46377) (сборная), третье — [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2826).


*[К оглавлению](#kvrm_contents)*

---

**X чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 20–21 апреля 2013 года в Ташкенте. <a name="chgk_2013"></a>

Победитель: **[«НМТТ» (Ташкент)](https://rating.chgk.info/teams/4864)**
- Усман Шарифходжаев
- Рустамхужа Саид-Аминов
- Александр Ли
- Акрам Икрамов
- Абдулазиз Джалилов
- Игорь Глущенко
- Алексей Акименко

Второе место заняла команда [«ParadoX»](https://rating.chgk.info/teams/4749) (Навои), третье — [«7Hz»](https://rating.chgk.info/teams/4156) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2362).


*[К оглавлению](#kvrm_contents)*

---

**IX чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 5–6 мая 2012 года в Ташкенте. <a name="chgk_2012"></a>

Победитель: **[«НМТТ» (Ташкент)](https://rating.chgk.info/teams/4864)**
- Усман Шарифходжаев
- Алексей Чолоков
- Рустамхужа Саид-Аминов
- Евгений Калюков
- Абдулазиз Джалилов
- Игорь Глущенко
- Хаким Батыралиев
- Алексей Акименко

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент), третье — [«Пахтакор»](https://rating.chgk.info/teams/28587) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2099).


*[К оглавлению](#kvrm_contents)*

---

**VIII чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 6–7 мая 2011 года в Ташкенте. <a name="chgk_2011"></a>

Победитель: **[«НМТТ» (Ташкент)](https://rating.chgk.info/teams/4864)**
- Усман Шарифходжаев
- Рустамхужа Саид-Аминов
- Александр Райков
- Илья Новиков
- Евгений Калюков
- Акрам Икрамов
- Абдулазиз Джалилов
- Игорь Глущенко
- Алексей Акименко

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент), третье — [«7Hz»](https://rating.chgk.info/teams/4156) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1775).


*[К оглавлению](#kvrm_contents)*

---

**VII чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 28–29 мая 2010 года в Ташкенте. <a name="chgk_2010"></a>

Победитель: **[«НМТТ» (Ташкент)](https://rating.chgk.info/teams/4864)**
- Алексей Чолоков
- Рустамхужа Саид-Аминов
- Александр Райков
- Акрам Икрамов
- Александр Друзь
- Абдулазиз Джалилов
- Игорь Глущенко
- Алексей Акименко

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент), третье — [«ParadoX»](https://rating.chgk.info/teams/4749) (Навои).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/665).


*[К оглавлению](#kvrm_contents)*

---

**VI чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 9 мая 2009 года в Ташкенте. <a name="chgk_2009"></a>

Победитель: **[«7Hz» (Ташкент)](https://rating.chgk.info/teams/4156)**
- Лейла Шахназарова
- Георгий Шахназаров
- Максим Соболевский
- Алексей Саркулов
- Никита Макаренко
- Юрий Идрисов
- Антонина Бударина
- Игорь Аипкин

Второе место заняла команда [«НМТТ»](https://rating.chgk.info/teams/4864) (Ташкент), третье — [«Брюссельские»](https://rating.chgk.info/teams/815) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/456).


*[К оглавлению](#kvrm_contents)*

---

**V чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 9–10 мая 2008 года в Ташкенте. <a name="chgk_2008"></a>

Победитель: **[«НМТТ» (Ташкент)](https://rating.chgk.info/teams/4864)**
- Алексей Чолоков
- Руслан Усманов
- Рустамхужа Саид-Аминов
- Александр Райков
- Акрам Икрамов
- Абдулазиз Джалилов
- Игорь Глущенко
- Саидакбар Гафуров
- Анна Алиева

Второе место заняла команда [«Мы»](https://rating.chgk.info/teams/2462) (Ташкент), третье — [«Veni Vidi Vici»](https://rating.chgk.info/teams/3449) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/340).


*[К оглавлению](#kvrm_contents)*

---

**IV чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 5 мая 2007 года в Ташкенте. <a name="chgk_2007"></a>

Победитель: **[«7Hz» (Ташкент)](https://rating.chgk.info/teams/4156)**
- Лейла Шахназарова
- Георгий Шахназаров
- Алексей Саркулов
- Александр Райков
- Агзамходжа Ибрагимов
- Антонина Бударина
- Игорь Аипкин

Второе место заняла команда [«Veni Vidi Vici»](https://rating.chgk.info/teams/3449) (Ташкент), третье — [«НМТТ»](https://rating.chgk.info/teams/4864) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/243).


*[К оглавлению](#kvrm_contents)*

---

**III чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 13 мая 2006 года в Ташкенте. <a name="chgk_2006"></a>

Победитель: **[«7Hz» (Ташкент)](https://rating.chgk.info/teams/4156)**
- Лейла Шахназарова
- Георгий Шахназаров
- Герман Стимбан
- Анастасия Пересыпкина
- Сергей Киргизов
- Антонина Бударина
- Игорь Аипкин

Второе место заняла команда [«НМТТ»](https://rating.chgk.info/teams/4864) (Ташкент), третье — [«Dream team»](https://rating.chgk.info/teams/3687) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/169).


*[К оглавлению](#kvrm_contents)*

---

**II чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл 23 апреля 2005 года в Ташкенте. <a name="chgk_2005"></a>

Победитель: **[«Брюссельские» (Ташкент)](https://rating.chgk.info/teams/815)**
- Мария Скляревская
- Евгений Полюдов
- Рустам Мирзаханов
- Владимир Клименко
- Джасурбек Гайбуллаев
- Гульнара Асямова
- Михаил Аношкин
- Роман Алиев

Второе место заняла команда [«Заковат-1»](https://rating.chgk.info/teams/3523) (Ташкент), третье — [«Veni Vidi Vici»](https://rating.chgk.info/teams/3449) (Ташкент).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/95).


*[К оглавлению](#kvrm_contents)*

---

**I чемпионат Узбекистана по спортивному «Что? Где? Когда?»** прошёл в 2004 году в Ташкенте. <a name="chgk_2004"></a>

Победитель: **[«Мы» (Ташкент)](https://rating.chgk.info/teams/2462)**
- Пётр Яковлев
- Дина Сагадиева
- Галина Прибыткова
- Рустам Ниязов
- Анаит Григорян
- Рим Валеев



*[К оглавлению](#kvrm_contents)*

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


**XV чемпионат Узбекистана по спортивной «Своей игре»** прошёл 21 февраля 2026 года в Ташкенте. <a name="ssi_2026"></a>

Победитель: **[Артём Семёнов](https://rating.chgk.info/player/28654)**

Второе место занял [Александр Ли](https://rating.chgk.info/player/18316), третье — [Егор Дружинин](https://rating.chgk.info/player/9801).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1Qr7GOSy2jy-oiloNYhx83lz4mvmrUcoeDUVDPT3yRiQ/edit?gid=1573363467#gid=1573363467). Больше информации о турнире — [здесь](https://t.me/chgknews/1375).


*[К оглавлению](#ssi_contents)*

---

**XIV чемпионат Узбекистана по спортивной «Своей игре»** прошёл 25 января 2025 года в Ташкенте. <a name="ssi_2025"></a>

Победитель: **[Тимур Кафиатуллин](https://rating.chgk.info/player/13782)**

Второе место занял [Павел Корнилов](https://rating.chgk.info/player/174012), третье — [Егор Дружинин](https://rating.chgk.info/player/9801).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1obYf9XLtdzMaUCsyclm8ePN3-WwJpYDlwt4_iqg4JwQ/edit?gid=1573363467#gid=1573363467). Больше информации о турнире — [здесь](https://t.me/chgknews/1027).


*[К оглавлению](#ssi_contents)*

---

**XIII чемпионат Узбекистана по спортивной «Своей игре»** прошёл 16 марта 2024 года в Ташкенте. <a name="ssi_2024"></a>

Победитель: **[Александр Ли](https://rating.chgk.info/player/18316)**

Второе место занял [Егор Дружинин](https://rating.chgk.info/player/9801), третье — [Тимур Кафиатуллин](https://rating.chgk.info/player/13782).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1fQ8xiH6y5hiwnn_eqgdSTYIdYFR6X0mkCON7PfgT7h8/edit?usp=sharing). Больше информации о турнире — [здесь](https://t.me/chgknews/765).


*[К оглавлению](#ssi_contents)*

---

**XII чемпионат Узбекистана по спортивной «Своей игре»** прошёл 23 февраля 2023 года в Ташкенте. <a name="ssi_2023"></a>

Победитель: **[Акрам Икрамов](https://rating.chgk.info/player/12482)**

Второе место занял [Егор Дружинин](https://rating.chgk.info/player/9801), третье — [Александр Ли](https://rating.chgk.info/player/18316).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1rzY7x0JCcM9Yaa0lBlAhJCEP5vY2sELek_5F554M9Cg/edit#gid=1573363467). Больше информации о турнире — [в этом телеграм-канале](https://t.me/iivtiivt/52) и [здесь](https://t.me/chgknews/442).


*[К оглавлению](#ssi_contents)*

---

**XI чемпионат Узбекистана по спортивной «Своей игре»** прошёл 6 февраля 2022 года в Ташкенте. <a name="ssi_2022"></a>

Победитель: **[Артём Семёнов](https://rating.chgk.info/player/28654)**

Второе место занял [Акрам Икрамов](https://rating.chgk.info/player/12482), третье — [Александр Ли](https://rating.chgk.info/player/18316). Больше информации о турнире — [в этом телеграм-канале](https://t.me/auluz/297).


*[К оглавлению](#ssi_contents)*

---

**X чемпионат Узбекистана по спортивной «Своей игре»** прошёл 31 января 2021 года в Ташкенте. <a name="ssi_2021"></a>

Победитель: **[Акрам Икрамов](https://rating.chgk.info/player/12482)**

Второе место занял [Александр Райков](https://rating.chgk.info/player/26586), третье — [Георгий Шванов](https://rating.chgk.info/player/131786). Больше информации о турнире — [в этом телеграм-канале](https://t.me/auluz/271).


*[К оглавлению](#ssi_contents)*

---

**IX чемпионат Узбекистана по спортивной «Своей игре»** прошёл 15 декабря 2019 года в Ташкенте. <a name="ssi_2019"></a>

Победитель: **[Акрам Икрамов](https://rating.chgk.info/player/12482)**

Второе место занял [Игорь Аипкин](https://rating.chgk.info/player/487), третье — [Сардор Ахмедов](https://rating.chgk.info/player/75099). Больше информации о турнире — [в этом телеграм-канале](https://t.me/auluz/224).


*[К оглавлению](#ssi_contents)*

---

**VIII чемпионат Узбекистана по спортивной «Своей игре»** прошёл 21–22 мая 2016 года в Ташкенте. <a name="ssi_2016"></a>

Победитель: **[Алексей Акименко](https://rating.chgk.info/player/535)**

*На этом турнире часть призёров неизвестна. Если вы что-то о них знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*


*[К оглавлению](#ssi_contents)*

---

**VII чемпионат Узбекистана по спортивной «Своей игре»** прошёл 28–29 марта 2015 года в Ташкенте. <a name="ssi_2015"></a>

Победитель: **[Наиль Фарукшин](https://rating.chgk.info/player/32901)**

Второе место занял [Александр Райков](https://rating.chgk.info/player/26586), третье — [Алексей Акименко](https://rating.chgk.info/player/535).


*[К оглавлению](#ssi_contents)*

---

**VI чемпионат Узбекистана по спортивной «Своей игре»** прошёл 22–23 марта 2014 года в Ташкенте. <a name="ssi_2014"></a>

Победитель: **[Наиль Фарукшин](https://rating.chgk.info/player/32901)**

Второе место занял [Александр Райков](https://rating.chgk.info/player/26586), третье — [Азизбек Юсуфов](https://rating.chgk.info/player/37142).


*[К оглавлению](#ssi_contents)*

---

**V чемпионат Узбекистана по спортивной «Своей игре»** прошёл 20–21 апреля 2013 года в Ташкенте. <a name="ssi_2013"></a>

Победитель: **[Герман Стимбан](https://rating.chgk.info/player/30579)**

Второе место занял [Хаким Батыралиев](https://rating.chgk.info/player/2673), третье — [Абдулазиз Джалилов](https://rating.chgk.info/player/9240).


*[К оглавлению](#ssi_contents)*

---

**IV чемпионат Узбекистана по спортивной «Своей игре»** прошёл 5–6 мая 2012 года в Ташкенте. <a name="ssi_2012"></a>

Победитель: **[Мурод Хамраев](https://rating.chgk.info/player/48843)**

Второе место занял [Александр Райков](https://rating.chgk.info/player/26586), третье — [Сергей Щербаков](https://rating.chgk.info/player/36821).


*[К оглавлению](#ssi_contents)*

---

**III чемпионат Узбекистана по спортивной «Своей игре»** прошёл 12 декабря 2010 года в Ташкенте. <a name="ssi_2010"></a>

Победитель: **[Александр Райков](https://rating.chgk.info/player/26586)**

Второе место занял [Игорь Степанян](https://rating.chgk.info/player/30537).

*На этом турнире часть призёров неизвестна. Если вы что-то о них знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*


*[К оглавлению](#ssi_contents)*

---

**II чемпионат Узбекистана по спортивной «Своей игре»** прошёл 13 декабря 2009 года в Ташкенте. <a name="ssi_2009"></a>

Победитель: **[Вадим Улитчев](https://rating.chgk.info/player/32589)**

Второе место занял [Александр Райков](https://rating.chgk.info/player/26586), третье — [Руслан Каримов](https://rating.chgk.info/player/13535).


*[К оглавлению](#ssi_contents)*

---

**I чемпионат Узбекистана по спортивной «Своей игре»** прошёл 7 июля 2007 года в Ташкенте. <a name="ssi_2007"></a>

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
<tr><td>2010</td><td>III чемпионат Узбекистана по ССИ</td><td>неизвестен обладатель третьего места.</td></tr>
<tr><td>2004</td><td>I чемпионат Узбекистана по ЧГК</td><td>неизвестны составы обладателей второго и третьего мест, точная дата проведения турнира.</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
