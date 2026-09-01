---
title: 2001–2019
weight: 1
bookToC: false
---

# Россия (2001–2019)

Чемпионаты России по спортивному ЧГК проводятся с 2001 года. Чемпионаты России по эрудит-квартету проводятся с 2012 года. Ниже можно увидеть статистику по всем призёрам — как командам, так и игрокам. Также в отдельных вкладках можно найти информацию о чемпионатах страны по той или иной дисциплине. Сейчас не хватает информации об итогах ЧРЭК 2013 и 2014 годов. Если вы что-то знаете о призёрах или их составах, напишите, пожалуйста, на почту <chgknews.info@gmail.com>.

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
  function tabFromHash(){
    var hash=(location.hash||"").replace(/^#/,"");
    if(!hash)return buttons[0]&&buttons[0].getAttribute("data-tab");
    if(document.getElementById("country-tab-"+hash))return hash;
    var el=document.getElementById(hash);
    if(el){
      var panel=el.closest(".country-tab-panel");
      if(panel&&panel.id.indexOf("country-tab-")===0)return panel.id.slice("country-tab-".length);
    }
    return buttons[0]&&buttons[0].getAttribute("data-tab");
  }
  show(tabFromHash());
  window.addEventListener("hashchange",function(){show(tabFromHash());});
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",wrapTabs);
else wrapTabs();
})();
</script>
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-chgk" aria-selected="false">Турниры по ЧГК</button><button type="button" role="tab" data-tab="game-ek" aria-selected="false">Турниры по ЭК</button><button type="button" role="tab" data-tab="game-ssi" aria-selected="false">Турниры по ССИ</button><button type="button" role="tab" data-tab="game-ssi_f" aria-selected="false">Турниры по ССИ с фальстартами</button><button type="button" role="tab" data-tab="missing-data" aria-selected="false">Нет данных</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th rowspan="2">Команда</th><th rowspan="2">Город</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">ЧГК</th><th colspan="3" style="text-align:center">ЭК</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/188">Команда Губанова</a></td>
<td>Санкт-Петербург</td>
<td>4</td>
<td>5</td>
<td>2</td>
<td>11</td>
<td>4</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/670">Ксеп</a></td>
<td>Москва</td>
<td>3</td>
<td>4</td>
<td>3</td>
<td>10</td>
<td>3</td>
<td>4</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/2">Афина</a></td>
<td>Москва</td>
<td>3</td>
<td>2</td>
<td>3</td>
<td>8</td>
<td>3</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/5">Команда Кузьмина</a></td>
<td>Москва</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>5</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1">Неспроста</a></td>
<td>Москва</td>
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
<td><a href="https://rating.chgk.info/teams/45556">Рабочее название</a></td>
<td>Санкт-Петербург</td>
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
<td><a href="https://rating.chgk.info/teams/49804">Борский корабел</a></td>
<td>Москва</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/168">Сборная Кирибати</a></td>
<td>Санкт-Петербург</td>
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
<td><a href="https://rating.chgk.info/teams/175">Транссфера</a></td>
<td>Санкт-Петербург</td>
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
<td><a href="https://rating.chgk.info/teams/26">ЛКИ</a></td>
<td>Москва</td>
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
<td><a href="https://rating.chgk.info/teams/55">Мираж</a></td>
<td>Самара</td>
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
<td><a href="https://rating.chgk.info/teams/312">Социал-демократы</a></td>
<td>Москва</td>
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
<td><a href="https://rating.chgk.info/teams/1008">Катус</a></td>
<td>Санкт-Петербург</td>
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
<td><a href="https://rating.chgk.info/teams/3951">Eclipse</a></td>
<td>Санкт-Петербург</td>
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
<td><a href="https://rating.chgk.info/teams/3">Команда Ильи Иткина</a></td>
<td>Москва</td>
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
<td><a href="https://rating.chgk.info/teams/27601">Самсон</a></td>
<td>Петергоф</td>
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
<td><a href="https://rating.chgk.info/teams/264">Джокер</a></td>
<td>Саратов</td>
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
<tr><th rowspan="2">Игрок</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">ЧГК</th><th colspan="3" style="text-align:center">ЭК</th><th colspan="3" style="text-align:center">ССИ</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/player/6212">Юрий Выменец</a></td>
<td>3</td>
<td>7</td>
<td>4</td>
<td>14</td>
<td>3</td>
<td>7</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3207">Ольга Берёзкина</a></td>
<td>5</td>
<td>5</td>
<td>3</td>
<td>13</td>
<td>4</td>
<td>5</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18332">Александр Либер</a></td>
<td>4</td>
<td>2</td>
<td>7</td>
<td>13</td>
<td>4</td>
<td>2</td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18036">Михаил Левандовский</a></td>
<td>4</td>
<td>2</td>
<td>6</td>
<td>12</td>
<td>4</td>
<td>2</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8333">Антон Губанов</a></td>
<td>4</td>
<td>5</td>
<td>1</td>
<td>10</td>
<td>4</td>
<td>5</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20207">Михаил Матвеев</a></td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>10</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22935">Илья Новиков</a></td>
<td>3</td>
<td>4</td>
<td>3</td>
<td>10</td>
<td>3</td>
<td>4</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20691">Станислав Мереминский</a></td>
<td>3</td>
<td>4</td>
<td>3</td>
<td>10</td>
<td>3</td>
<td>4</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25882">Максим Поташев</a></td>
<td>3</td>
<td>2</td>
<td>3</td>
<td>8</td>
<td>3</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22482">Роман Немучинский</a></td>
<td>3</td>
<td>2</td>
<td>3</td>
<td>8</td>
<td>3</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21487">Борис Моносов</a></td>
<td>2</td>
<td>5</td>
<td>1</td>
<td>8</td>
<td>2</td>
<td>5</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27403">Максим Руссо</a></td>
<td>5</td>
<td>0</td>
<td>2</td>
<td>7</td>
<td>5</td>
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
<td><a href="https://rating.chgk.info/player/30990">Пётр Сухачёв</a></td>
<td>4</td>
<td>0</td>
<td>3</td>
<td>7</td>
<td>4</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7008">Алексей Гилёв</a></td>
<td>3</td>
<td>2</td>
<td>2</td>
<td>7</td>
<td>3</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13551">Вадим Карлинский</a></td>
<td>3</td>
<td>1</td>
<td>3</td>
<td>7</td>
<td>3</td>
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
<td><a href="https://rating.chgk.info/player/3159">Илья Бер</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34846">Антон Чернин</a></td>
<td>2</td>
<td>2</td>
<td>3</td>
<td>7</td>
<td>2</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4270">Александра Брутер</a></td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>6</td>
<td>4</td>
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
<td><a href="https://rating.chgk.info/player/28751">Иван Семушин</a></td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>6</td>
<td>4</td>
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
<td><a href="https://rating.chgk.info/player/30270">Сергей Спешков</a></td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>6</td>
<td>4</td>
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
<td><a href="https://rating.chgk.info/player/30475">Владимир Степанов</a></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>6</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/707">Елена Александрова</a></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>6</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4063">Дмитрий Борок</a></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>6</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4878">Сергей Вакуленко</a></td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>6</td>
<td>2</td>
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
<td><a href="https://rating.chgk.info/player/29399">Александр Скородумов</a></td>
<td>1</td>
<td>4</td>
<td>1</td>
<td>6</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30152">Артём Сорожкин</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>5</td>
<td>4</td>
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
<td><a href="https://rating.chgk.info/player/17050">Андрей Кузьмин</a></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>5</td>
<td>3</td>
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
<td><a href="https://rating.chgk.info/player/5935">Павел Володин</a></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>5</td>
<td>3</td>
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
<td><a href="https://rating.chgk.info/player/29800">Антон Снятковский</a></td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>5</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1585">Юлия Архангельская</a></td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>5</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2935">Анатолий Белкин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32979">Виталий Фёдоров</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18935">Дмитрий Лурье</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35065">Борис Чигидин</a></td>
<td>2</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>3</td>
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
<td>4</td>
<td>5</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26089">Ирина Прокофьева</a></td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>5</td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15456">Сергей Коновалов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22799">Сергей Николенко</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27822">Михаил Савченков</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>4</td>
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
<td><a href="https://rating.chgk.info/player/16332">Николай Крапиль</a></td>
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
<td><a href="https://rating.chgk.info/player/15442">Дмитрий Коноваленко</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28513">Владимир Севриновский</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2694">Игорь Бахарев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15727">Александр Коробейников</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3671">Алексей Богословский</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15664">Кирилл Корконосенко</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37047">Мария Юнгер</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3270">Юрий Бершидский</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1560">Евгений Арутюнов</a></td>
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
<td><a href="https://rating.chgk.info/player/21580">Михаил Морозов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8082">Сергей Григ</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14025">Александра Киланова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23178">Елизавета Овдеенко</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20612">Валентин Мельников</a></td>
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
<td><a href="https://rating.chgk.info/player/10768">Дмитрий Жарков</a></td>
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
<td><a href="https://rating.chgk.info/player/35001">Юрий Черушев</a></td>
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
<td><a href="https://rating.chgk.info/player/23579">Елена Орлова</a></td>
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
<td><a href="https://rating.chgk.info/player/36497">Сергей Шоргин</a></td>
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
<td><a href="https://rating.chgk.info/player/9808">Александр Друзь</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4801">Алексей Вавилов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2620">Михаил Басс</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10066">Михаил Дюба</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8909">Фёдор Двинятин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27009">Александр Рождествин</a></td>
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
<td><a href="https://rating.chgk.info/player/8777">Анастасия Данелянц</a></td>
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
<td><a href="https://rating.chgk.info/player/31355">Антон Тахтаров</a></td>
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
<td><a href="https://rating.chgk.info/player/27177">Вероника Ромашова</a></td>
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
<td><a href="https://rating.chgk.info/player/27853">Владимир Садов</a></td>
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
<td><a href="https://rating.chgk.info/player/932">Григорий Алхазов</a></td>
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
<td><a href="https://rating.chgk.info/player/24127">Денис Паншин</a></td>
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
<td><a href="https://rating.chgk.info/player/3083">Дмитрий Белявский</a></td>
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
<td><a href="https://rating.chgk.info/player/2454">Мария Баранчикова</a></td>
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
<td><a href="https://rating.chgk.info/player/24290">Мария Пастухова</a></td>
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
<td><a href="https://rating.chgk.info/player/2938">Владимир Белкин</a></td>
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
<td><a href="https://rating.chgk.info/player/20260">Дарья Русакова</a></td>
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
<td><a href="https://rating.chgk.info/player/49151">Ирина Оловянная</a></td>
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
<td><a href="https://rating.chgk.info/player/1603">Лариса Архипова</a></td>
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
<td><a href="https://rating.chgk.info/player/21805">Михаил Мун</a></td>
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
<td><a href="https://rating.chgk.info/player/9785">Владислав Дронов</a></td>
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
<td><a href="https://rating.chgk.info/player/32004">Иван Топчий</a></td>
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
<td><a href="https://rating.chgk.info/player/3645">Кирилл Богловский</a></td>
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
<td><a href="https://rating.chgk.info/player/19599">Павел Малышев</a></td>
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
<td><a href="https://rating.chgk.info/player/25724">Юрий Попов</a></td>
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
<td><a href="https://rating.chgk.info/player/27497">Александр Рыжанов</a></td>
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
<td><a href="https://rating.chgk.info/player/27989">Александр Салита</a></td>
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
<td><a href="https://rating.chgk.info/player/19902">Алексей Маркин</a></td>
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
<td><a href="https://rating.chgk.info/player/18198">Андрей Ленский</a></td>
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
<td><a href="https://rating.chgk.info/player/23983">Борис Паленовский</a></td>
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
<td><a href="https://rating.chgk.info/player/6892">Дмитрий Герасимов</a></td>
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
<td><a href="https://rating.chgk.info/player/76497">Игорь Сиволоб</a></td>
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
<td><a href="https://rating.chgk.info/player/9809">Инна Друзь</a></td>
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
<td><a href="https://rating.chgk.info/player/14544">Константин Кноп</a></td>
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
<td><a href="https://rating.chgk.info/player/9810">Марина Друзь</a></td>
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
<td><a href="https://rating.chgk.info/player/15226">Мария Колосовская</a></td>
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
<td><a href="https://rating.chgk.info/player/22357">Мария Наумова</a></td>
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
<td><a href="https://rating.chgk.info/player/34219">Олег Христенко</a></td>
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
<td><a href="https://rating.chgk.info/player/23863">Роман Павлов</a></td>
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
<td><a href="https://rating.chgk.info/player/28729">Роман Семизаров</a></td>
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
<td><a href="https://rating.chgk.info/player/10660">Сергей Ефимов</a></td>
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
<td><a href="https://rating.chgk.info/player/31184">Эльман Талыбов</a></td>
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
<td><a href="https://rating.chgk.info/player/26798">Анна Резникова</a></td>
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
<td><a href="https://rating.chgk.info/player/4121">Антон Бочкарёв</a></td>
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
<td><a href="https://rating.chgk.info/player/15811">Владислав Король</a></td>
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
<td><a href="https://rating.chgk.info/player/3096">Иван Беляев</a></td>
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
<td><a href="https://rating.chgk.info/player/23020">Наталия Новыш</a></td>
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
<td><a href="https://rating.chgk.info/player/12987">Пётр Казённов</a></td>
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
<td><a href="https://rating.chgk.info/player/20001">Александр Мартынов</a></td>
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
<td><a href="https://rating.chgk.info/player/21698">Александр Мосягин</a></td>
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
<td><a href="https://rating.chgk.info/player/23737">Андрей Островский</a></td>
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
<td><a href="https://rating.chgk.info/player/2942">Анна Белкина</a></td>
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
<td><a href="https://rating.chgk.info/player/65525">Антон Исупов</a></td>
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
<td><a href="https://rating.chgk.info/player/37694">Владимир Молчанов</a></td>
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
<td><a href="https://rating.chgk.info/player/12119">Дмитрий Иванов</a></td>
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
<td><a href="https://rating.chgk.info/player/24384">Евгений Пашковский</a></td>
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
<td><a href="https://rating.chgk.info/player/12770">Илья Иткин</a></td>
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
<td><a href="https://rating.chgk.info/player/29032">Максим Сидоров</a></td>
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
<td><a href="https://rating.chgk.info/player/13631">Мария Карпова</a></td>
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
<td><a href="https://rating.chgk.info/player/49171">Николай Поникаров</a></td>
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
<td><a href="https://rating.chgk.info/player/27622">Николай Рябых</a></td>
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
<td><a href="https://rating.chgk.info/player/49168">Олег Виноградов</a></td>
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
<td>Олег Карпов</td>
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
<td><a href="https://rating.chgk.info/player/2005">Пётр Бавин</a></td>
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
<td><a href="https://rating.chgk.info/player/4551">Светлана Бурлак</a></td>
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
<td><a href="https://rating.chgk.info/player/32728">Александр Успанов</a></td>
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
<td><a href="https://rating.chgk.info/player/21418">Виктория Моключенко</a></td>
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
<td><a href="https://rating.chgk.info/player/12160">Михаил Иванов</a></td>
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
<td><a href="https://rating.chgk.info/player/17746">Михаил Лазарев</a></td>
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
<td><a href="https://rating.chgk.info/player/32730">Ольга Успанова</a></td>
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
<td><a href="https://rating.chgk.info/player/2005">Пётр Бавин</a></td>
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
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-chgk"></div>

<a id="game-chgk"></a>

- [XIX чемпионат России по спортивному ЧГК (2019)](#chgk_2019)
- [XVIII чемпионат России по спортивному ЧГК (2018)](#chgk_2018)
- [XVII чемпионат России по спортивному ЧГК (2017)](#chgk_2017)
- [XVI чемпионат России по спортивному ЧГК (2016)](#chgk_2016)
- [XV чемпионат России по спортивному ЧГК (2015)](#chgk_2015)
- [XIV чемпионат России по спортивному ЧГК (2014)](#chgk_2014)
- [XIII чемпионат России по спортивному ЧГК (2013)](#chgk_2013)
- [XII чемпионат России по спортивному ЧГК (2012)](#chgk_2012)
- [XI чемпионат России по спортивному ЧГК (2011)](#chgk_2011)
- [X чемпионат России по спортивному ЧГК (2010)](#chgk_2010)
- [IX чемпионат России по спортивному ЧГК (2009)](#chgk_2009)
- [VIII чемпионат России по спортивному ЧГК (2008)](#chgk_2008)
- [VII чемпионат России по спортивному ЧГК (2007)](#chgk_2007)
- [VI чемпионат России по спортивному ЧГК (2006)](#chgk_2006)
- [V чемпионат России по спортивному ЧГК (2005)](#chgk_2005)
- [IV чемпионат России по спортивному ЧГК (2004)](#chgk_2004)
- [III чемпионат России по спортивному ЧГК (2003)](#chgk_2003)
- [II чемпионат России по спортивному ЧГК (2002)](#chgk_2002)
- [I чемпионат России по спортивному ЧГК (2001)](#chgk_2001)


**XIX чемпионат России по спортивному «Что? Где? Когда?»** прошёл 18–19 мая 2019 года в Москве. <a name="chgk_2019"></a>

Победитель: **[«Борский корабел» (Москва)](https://rating.chgk.info/teams/49804)**
- Сергей Спешков
- Артём Сорожкин
- Иван Семушин
- Михаил Савченков
- Максим Руссо
- Александра Брутер

Второе место заняла команда [«Сборная Кирибати»](https://rating.chgk.info/teams/168) (Санкт-Петербург), третье — [«Рабочее название»](https://rating.chgk.info/teams/45556) (Санкт-Петербург).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5465), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/5276).

---

**XVIII чемпионат России по спортивному «Что? Где? Когда?»** прошёл 30 апреля–1 мая 2018 года в Санкт-Петербурге. <a name="chgk_2018"></a>

Победитель: **[«Борский корабел» (Москва)](https://rating.chgk.info/teams/49804)**
- Сергей Спешков
- Артём Сорожкин
- Иван Семушин
- Михаил Савченков
- Максим Руссо
- Александра Брутер

Второе место заняла команда [«Ксеп»](https://rating.chgk.info/teams/670) (Москва), третье — [«Рабочее название»](https://rating.chgk.info/teams/45556) (Санкт-Петербург).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4936), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/856).

---

**XVII чемпионат России по спортивному «Что? Где? Когда?»** прошёл 7–8 мая 2017 года в Санкт-Петербурге. <a name="chgk_2017"></a>

Победитель: **[«Борский корабел» (Москва)](https://rating.chgk.info/teams/49804)**
- Артём Сорожкин
- Иван Семушин
- Михаил Савченков
- Максим Руссо
- Елизавета Овдеенко
- Александра Брутер

Второе место заняла команда [«Рабочее название»](https://rating.chgk.info/teams/45556) (Санкт-Петербург), третье — [«Команда Губанова»](https://rating.chgk.info/teams/188) (Санкт-Петербург).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4247), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/1184).

---

**XVI чемпионат России по спортивному «Что? Где? Когда?»** прошёл 7–8 мая 2016 года в Воронеже. <a name="chgk_2016"></a>

Победитель: **[«Борский корабел» (Москва)](https://rating.chgk.info/teams/49804)**
- Артём Сорожкин
- Иван Семушин
- Михаил Савченков
- Максим Руссо
- Елизавета Овдеенко
- Александра Брутер

Второе место заняла команда [«Рабочее название»](https://rating.chgk.info/teams/45556) (Санкт-Петербург), третье — [«Мираж»](https://rating.chgk.info/teams/55) (Самара).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3825), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/1525).

---

**XV чемпионат России по спортивному «Что? Где? Когда?»** прошёл 16–17 мая 2015 года в Санкт-Петербурге. <a name="chgk_2015"></a>

Победитель: **[«Команда Губанова» (Санкт-Петербург)](https://rating.chgk.info/teams/188)**
- Борис Моносов
- Михаил Матвеев
- Антон Губанов
- Алексей Гилёв
- Сергей Вакуленко
- Ольга Берёзкина

Второе место заняла команда [«Ксеп»](https://rating.chgk.info/teams/670) (Москва), третье — [«Рабочее название»](https://rating.chgk.info/teams/45556) (Санкт-Петербург).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3099), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/1918).

---

**XIV чемпионат России по спортивному «Что? Где? Когда?»** прошёл 7–8 марта 2014 года в Санкт-Петербурге. <a name="chgk_2014"></a>

Победитель: **[«Ксеп» (Москва)](https://rating.chgk.info/teams/670)**
- Сергей Спешков
- Илья Новиков
- Роман Немучинский
- Станислав Мереминский
- Николай Крапиль
- Илья Бер
- Юлия Архангельская

Второе место заняла команда [«Команда Губанова»](https://rating.chgk.info/teams/188) (Санкт-Петербург), третье — [«ЛКИ»](https://rating.chgk.info/teams/26) (Москва).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2813), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/2480).

---

**XIII чемпионат России по спортивному «Что? Где? Когда?»** прошёл 12–13 апреля 2013 года в Пскове. <a name="chgk_2013"></a>

Победитель: **[«Ксеп» (Москва)](https://rating.chgk.info/teams/670)**
- Сергей Спешков
- Илья Новиков
- Роман Немучинский
- Станислав Мереминский
- Николай Крапиль
- Илья Бер
- Юлия Архангельская

Второе место заняла команда [«Команда Губанова»](https://rating.chgk.info/teams/188) (Санкт-Петербург), третье — [«Афина»](https://rating.chgk.info/teams/2) (Москва).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2117), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/2867).

---

**XII чемпионат России по спортивному «Что? Где? Когда?»** прошёл 18–19 мая 2012 года в Москве. <a name="chgk_2012"></a>

Победитель: **[«Команда Губанова» (Санкт-Петербург)](https://rating.chgk.info/teams/188)**
- Борис Моносов
- Михаил Матвеев
- Антон Губанов
- Алексей Гилёв
- Юрий Выменец
- Ольга Берёзкина

Второе место заняла команда [«Сборная Кирибати»](https://rating.chgk.info/teams/168) (Санкт-Петербург), третье — [«Ксеп»](https://rating.chgk.info/teams/670) (Москва).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1983), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3239).

---

**XI чемпионат России по спортивному «Что? Где? Когда?»** прошёл 5–6 марта 2011 года в Нижний Новгороде. <a name="chgk_2011"></a>

Победитель: **[«Афина» (Москва)](https://rating.chgk.info/teams/2)**
- Антон Чернин
- Пётр Сухачёв
- Владимир Степанов
- Максим Поташев
- Александр Либер
- Михаил Левандовский
- Вадим Карлинский

Второе место заняла команда [«Мираж»](https://rating.chgk.info/teams/55) (Самара), третье — [«Команда Губанова»](https://rating.chgk.info/teams/188) (Санкт-Петербург).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1710), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3889).

---

**X чемпионат России по спортивному «Что? Где? Когда?»** прошёл 19–20 февраля 2010 года в Москве. <a name="chgk_2010"></a>

Победитель: **[«Команда Губанова» (Санкт-Петербург)](https://rating.chgk.info/teams/188)**
- Александр Скородумов
- Михаил Матвеев
- Антон Губанов
- Алексей Гилёв
- Юрий Выменец
- Ольга Берёзкина

Второе место заняла команда [«Сборная Кирибати»](https://rating.chgk.info/teams/168) (Санкт-Петербург). Третье место разделили команды [«Афина»](https://rating.chgk.info/teams/2) (Москва) и [«Команда Кузьмина»](https://rating.chgk.info/teams/5) (Москва).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/583), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4145).

---

**IX чемпионат России по спортивному «Что? Где? Когда?»** прошёл 20–21 марта 2009 года в Санкт-Петербурге. <a name="chgk_2009"></a>

Победитель: **[«Команда Кузьмина» (Москва)](https://rating.chgk.info/teams/5)**
- Борис Чигидин
- Пётр Сухачёв
- Александр Либер
- Михаил Левандовский
- Андрей Кузьмин
- Евгений Калюков
- Павел Володин
- Дмитрий Борок

Второе место разделили команды [«ЛКИ»](https://rating.chgk.info/teams/26) (Москва) и [«Катус»](https://rating.chgk.info/teams/1008) (Санкт-Петербург).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/484), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4542).

---

**VIII чемпионат России по спортивному «Что? Где? Когда?»** прошёл 8–9 марта 2008 года в Москве. <a name="chgk_2008"></a>

Победитель: **[«Афина» (Москва)](https://rating.chgk.info/teams/2)**
- Антон Чернин
- Владимир Степанов
- Максим Руссо
- Максим Поташев
- Михаил Мун
- Вадим Карлинский
- Елена Александрова

Второе место заняла команда [«Команда Губанова»](https://rating.chgk.info/teams/188) (Санкт-Петербург). Третье место разделили команды [«Команда Кузьмина»](https://rating.chgk.info/teams/5) (Москва) и [«Ксеп»](https://rating.chgk.info/teams/670) (Москва).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/315), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4858).

---

**VII чемпионат России по спортивному «Что? Где? Когда?»** прошёл 23–24 февраля 2007 года в Казани. <a name="chgk_2007"></a>

Победитель: **[«Команда Кузьмина» (Москва)](https://rating.chgk.info/teams/5)**
- Борис Чигидин
- Пётр Сухачёв
- Александр Либер
- Михаил Левандовский
- Андрей Кузьмин
- Павел Володин

Второе место разделили команды [«Неспроста»](https://rating.chgk.info/teams/1) (Москва) и [«Сборная Кирибати»](https://rating.chgk.info/teams/168) (Санкт-Петербург).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/226), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4531).

---

**VI чемпионат России по спортивному «Что? Где? Когда?»** прошёл 25 февраля 2006 года в Саранске. <a name="chgk_2006"></a>

Победитель: **[«Неспроста» (Москва)](https://rating.chgk.info/teams/1)**
- Виталий Фёдоров
- Антон Снятковский
- Валентин Мельников
- Дмитрий Лурье
- Юрий Бершидский
- Анатолий Белкин

Второе место разделили команды [«Команда Губанова»](https://rating.chgk.info/teams/188) (Санкт-Петербург) и [«Ксеп»](https://rating.chgk.info/teams/670) (Москва).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/141), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4233).

---

**V чемпионат России по спортивному «Что? Где? Когда?»** прошёл 25–26 февраля 2005 года в Москве. <a name="chgk_2005"></a>

Победитель: **[«Команда Кузьмина» (Москва)](https://rating.chgk.info/teams/5)**
- Пётр Сухачёв
- Александр Либер
- Михаил Левандовский
- Андрей Кузьмин
- Павел Володин
- Лариса Архипова

Второе место заняла команда [«Команда Губанова»](https://rating.chgk.info/teams/188) (Санкт-Петербург), третье — [«Неспроста»](https://rating.chgk.info/teams/1) (Москва).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/76), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3922).

---

**IV чемпионат России по спортивному «Что? Где? Когда?»** прошёл 20–21 февраля 2004 года в Санкт-Петербурге. <a name="chgk_2004"></a>

Победитель: **[«Неспроста» (Москва)](https://rating.chgk.info/teams/1)**
- Сергей Шоргин
- Виталий Фёдоров
- Дмитрий Лурье
- Сергей Вакуленко
- Юрий Бершидский
- Анатолий Белкин
- Евгений Арутюнов

Второе место разделили команды [«Афина»](https://rating.chgk.info/teams/2) (Москва) и [«Ксеп»](https://rating.chgk.info/teams/670) (Москва).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/22), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3371).

---

**III чемпионат России по спортивному «Что? Где? Когда?»** прошёл 15–16 февраля 2003 года в Москве. <a name="chgk_2003"></a>

Победитель: **[«Команда Губанова» (Санкт-Петербург)](https://rating.chgk.info/teams/188)**
- Ирина Оловянная
- Дарья Русакова
- Дмитрий Жарков
- Антон Губанов
- Юрий Выменец
- Ольга Берёзкина

Второе место заняла команда [«Афина»](https://rating.chgk.info/teams/2) (Москва). Третье место разделили команды [«Команда Ильи Иткина»](https://rating.chgk.info/teams/3) (Москва) и [«Ксеп»](https://rating.chgk.info/teams/670) (Москва).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1369), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/2771).

---

**II чемпионат России по спортивному «Что? Где? Когда?»** прошёл 31 января–2 февраля 2002 года в Москве. <a name="chgk_2002"></a>

Победитель: **[«Ксеп» (Москва)](https://rating.chgk.info/teams/670)**
- Антон Снятковский
- Владимир Севриновский
- Илья Новиков
- Роман Немучинский
- Станислав Мереминский
- Игорь Бахарев

Второе место заняла команда [«Транссфера»](https://rating.chgk.info/teams/175) (Санкт-Петербург). Третье место разделили команды [«Неспроста»](https://rating.chgk.info/teams/1) (Москва) и [«Афина»](https://rating.chgk.info/teams/2) (Москва).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1224), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/2247).

---

**I чемпионат России по спортивному «Что? Где? Когда?»** прошёл 2–3 февраля 2001 года в Москве. <a name="chgk_2001"></a>

Победитель: **[«Афина» (Москва)](https://rating.chgk.info/teams/2)**
- Юрий Черушев
- Максим Поташев
- Елена Орлова
- Дмитрий Коноваленко
- Вадим Карлинский
- Владимир Белкин
- Елена Александрова

Второе место заняла команда [«Транссфера»](https://rating.chgk.info/teams/175) (Санкт-Петербург), третье — [«Самсон»](https://rating.chgk.info/teams/27601) (Петергоф).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1082), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/1630).

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ek"></div>

<a id="game-ek"></a>

- [I чемпионат России по ЭК (2012)](#ek_2012)


**I чемпионат России по эрудит-квартету** прошёл 18–19 мая 2012 года в Москве. <a name="ek_2012"></a>

Победитель: **[«Социал-демократы» (Москва)](https://rating.chgk.info/teams/312)**
- Артём Сорожкин
- Ольга Берёзкина
- Владислав Дронов
- Иван Топчий
- Юрий Попов
- Павел Малышев

Второе место заняла команда [«Eclipse»](https://rating.chgk.info/teams/3951) (Санкт-Петербург), третье — [«Джокер»](https://rating.chgk.info/teams/264) (Саратов).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1MLb11WySRRX6yP6rXSUXF4JAuO78VtB7_zkmTZPLzRM/edit?gid=8#gid=8).

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ssi"></div>

<a id="game-ssi"></a>

- [I чемпионат России по ССИ (2007)](#ssi_2007)


**I чемпионат России по спортивной «Своей игре»** прошёл 15–16 сентября 2007 года в Великих Луках. <a name="ssi_2007"></a>

Победитель: **[Кирилл Богловский](https://rating.chgk.info/player/3645)**

Второе место занял [Дмитрий Борок](https://rating.chgk.info/player/4063), третье — [Евгений Калюков](https://rating.chgk.info/player/13196).

Полные результаты можно найти [на этой странице](http://si-chross.chgk.info/index.php?page=results_wf), вопросы турнира можно почитать [здесь](https://db.chgk.info/tour/russv07). Больше информации о турнире — [на сайте чемпионата](http://si-chross.chgk.info/index.php).

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ssi_f"></div>

<a id="game-ssi_f"></a>

- [I чемпионат России по ССИ с фальстартами (2007)](#ssi_f_2007)


**I чемпионат России по спортивной «Своей игре» с фальстартами** прошёл 15–16 сентября 2007 года в Великих Луках. <a name="ssi_f_2007"></a>

Победитель: **[Дмитрий Борок](https://rating.chgk.info/player/4063)**

Второе место занял [Пётр Казённов](https://rating.chgk.info/player/12987), третье — [Евгений Калюков](https://rating.chgk.info/player/13196).

Полные результаты можно найти [на этой странице](http://si-chross.chgk.info/index.php?page=result_falstart), вопросы турнира можно почитать [здесь](https://db.chgk.info/tour/russv07). Больше информации о турнире — [на сайте чемпионата](http://si-chross.chgk.info/index.php).

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
<tr><td>2009</td><td><a href="https://rating.chgk.info/tournament/484">IX чемпионат России по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2007</td><td><a href="https://rating.chgk.info/tournament/226">VII чемпионат России по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2006</td><td><a href="https://rating.chgk.info/tournament/141">VI чемпионат России по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2004</td><td><a href="https://rating.chgk.info/tournament/22">IV чемпионат России по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
