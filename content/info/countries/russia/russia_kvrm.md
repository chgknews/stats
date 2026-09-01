---
title: ЧР по ИИ
weight: 1
bookToC: false
---

# ЧР по интеллектуальным играм

ЧР по интеллектуальным играм проводятся с 2025 года. Ниже можно увидеть статистику по всем призёрам — как командам, так и игрокам. Также в отдельных вкладках можно найти информацию о чемпионатах страны по той или иной дисциплине. Чуть больше информации об истории турнира можно найти в [этой гуглтаблице](https://docs.google.com/spreadsheets/d/1s6YqakSEDwkGOYQsDWwT4oKGeK-v-8U7WCTbeZ_i6dk/edit?gid=0#gid=0).

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-ek" aria-selected="false">Турниры по ЭК</button><button type="button" role="tab" data-tab="game-ksi" aria-selected="false">Турниры по КСИ</button><button type="button" role="tab" data-tab="game-kvrm" aria-selected="false">Турниры по КВРМ</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th rowspan="2">Команда</th><th rowspan="2">Город</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">КВРМ</th><th colspan="3" style="text-align:center">ЭК</th><th colspan="3" style="text-align:center">КСИ</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/49804">Борский корабел</a></td>
<td>Москва</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/45556">Рабочее название</a></td>
<td>Санкт-Петербург</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/27177">Призраки Коши</a></td>
<td>Санкт-Петербург</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/4109">Первая сборная</a></td>
<td>Москва</td>
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
<td><a href="https://rating.chgk.info/teams/45174">София</a></td>
<td>Саранск</td>
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
<td><a href="https://rating.chgk.info/teams/71595">Я просто медленно пишу</a></td>
<td>Москва</td>
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
<td><a href="https://rating.chgk.info/teams/103505">Рождённый с ПТСР</a></td>
<td>Раменское</td>
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
<td><a href="https://rating.chgk.info/teams/75592">Тихие Тигры</a></td>
<td>Мытищи</td>
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
<td><a href="https://rating.chgk.info/teams/45470">ff</a></td>
<td>Москва</td>
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
<td><a href="https://rating.chgk.info/teams/52143">Дальше уже</a></td>
<td>Екатеринбург</td>
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
<div class="country-tab-start" data-tab="players"></div>

<a id="players"></a>

<table>
<thead>
<tr><th rowspan="2">Игрок</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">КВРМ</th><th colspan="3" style="text-align:center">ЭК</th><th colspan="3" style="text-align:center">КСИ</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/player/37761">Дмитрий Сахаров</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28751">Иван Семушин</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33620">Руслан Хаиткулов</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30270">Сергей Спешков</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4270">Александра Брутер</a></td>
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
<td><a href="https://rating.chgk.info/player/27403">Максим Руссо</a></td>
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
<td><a href="https://rating.chgk.info/player/61400">Алексей Андрюшин</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18332">Александр Либер</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26640">Вадим Раскумандрин</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26089">Ирина Прокофьева</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10145">Сергей Евсеев</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15456">Сергей Коновалов</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22799">Сергей Николенко</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/218493">Сергей Шеремет</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23321">Дмитрий Ожигов</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37718">Дмитрий Петров</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25819">Николай Порцель</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31493">Сергей Терентьев</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33032">Татьяна Фёдорова</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6212">Юрий Выменец</a></td>
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
<td><a href="https://rating.chgk.info/player/15727">Александр Коробейников</a></td>
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
<td><a href="https://rating.chgk.info/player/69394">Александр Талюк</a></td>
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
<td><a href="https://rating.chgk.info/player/134506">Игорь Кулешов</a></td>
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
<td><a href="https://rating.chgk.info/player/107161">Карина Файзуллина</a></td>
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
<td><a href="https://rating.chgk.info/player/34936">Кирилл Чернышев</a></td>
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
<td><a href="https://rating.chgk.info/player/25177">Никита Поверинов</a></td>
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
<td><a href="https://rating.chgk.info/player/86795">Павел Казначеев</a></td>
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
<td><a href="https://rating.chgk.info/player/40877">Ринат Сибаев</a></td>
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
<td><a href="https://rating.chgk.info/player/22808">Александр Никольский</a></td>
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
<td><a href="https://rating.chgk.info/player/88217">Андрей Судаков</a></td>
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
<td><a href="https://rating.chgk.info/player/173280">Анна Селиманкина</a></td>
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
<td><a href="https://rating.chgk.info/player/20196">Виктор Масягин</a></td>
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
<td><a href="https://rating.chgk.info/player/31038">Владимир Сушков</a></td>
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
<td><a href="https://rating.chgk.info/player/17969">Денис Лашин</a></td>
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
<td><a href="https://rating.chgk.info/player/4063">Дмитрий Борок</a></td>
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
<td><a href="https://rating.chgk.info/player/173230">Дмитрий Ковалев</a></td>
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
<td><a href="https://rating.chgk.info/player/238962">Максим Круглов</a></td>
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
<td><a href="https://rating.chgk.info/player/33146">Максим Феоктистов</a></td>
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
<td><a href="https://rating.chgk.info/player/156613">Наталия Зайнуллина</a></td>
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
<td><a href="https://rating.chgk.info/player/19666">Станислав Мальчёнков</a></td>
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
<td><a href="https://rating.chgk.info/player/173568">Татьяна Захарова</a></td>
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
<td><a href="https://rating.chgk.info/player/161388">Александр Брусенцев</a></td>
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
<td><a href="https://rating.chgk.info/player/199749">Алексей Раевский</a></td>
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
<td><a href="https://rating.chgk.info/player/53689">Антон Тилипман</a></td>
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
<td><a href="https://rating.chgk.info/player/224772">Артур Горбачёв</a></td>
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
<td><a href="https://rating.chgk.info/player/155079">Артём Авилов</a></td>
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
<td><a href="https://rating.chgk.info/player/62299">Даниил Удимов</a></td>
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
<td><a href="https://rating.chgk.info/player/23629">Дмитрий Осипков</a></td>
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
<td><a href="https://rating.chgk.info/player/63529">Дмитрий Тарарыков</a></td>
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
<td><a href="https://rating.chgk.info/player/74001">Игорь Мокин</a></td>
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
<td><a href="https://rating.chgk.info/player/147450">Максим Салихов</a></td>
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
<td><a href="https://rating.chgk.info/player/34644">Надежда Чеботкова</a></td>
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
<td><a href="https://rating.chgk.info/player/33236">Сергей Филин</a></td>
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
<td><a href="https://rating.chgk.info/player/39596">Александр Лавренов</a></td>
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
<td><a href="https://rating.chgk.info/player/51715">Анвар Мухаметкалиев</a></td>
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
<td><a href="https://rating.chgk.info/player/184810">Андрей Петров</a></td>
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
<td><a href="https://rating.chgk.info/player/62720">Артём Шилов</a></td>
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
<td><a href="https://rating.chgk.info/player/128367">Дмитрий Григорьев</a></td>
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
<td><a href="https://rating.chgk.info/player/234426">Дмитрий Камышев</a></td>
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
<td><a href="https://rating.chgk.info/player/24384">Евгений Пашковский</a></td>
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
<td><a href="https://rating.chgk.info/player/66245">Евгения Гончарова</a></td>
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
<td><a href="https://rating.chgk.info/player/156146">Игорь Фасхеев</a></td>
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
<td><a href="https://rating.chgk.info/player/84935">Мария Пилюгина</a></td>
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
<td><a href="https://rating.chgk.info/player/16837">Наталья Кудряшова</a></td>
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
<td><a href="https://rating.chgk.info/player/43456">Сергей Васильченко</a></td>
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
<td><a href="https://rating.chgk.info/player/31384">Эльман Талыбов</a></td>
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
<div class="country-tab-start" data-tab="game-ek"></div>

<a id="game-ek"></a>

- [I ЧР по эрудит-квартету (2026)](#ek_2026)


**I ЧР по эрудит-квартету** прошёл 13–14 июня 2026 года в Москве. <a name="ek_2026"></a>

Победитель: **[«Борский корабел» (Москва)](https://rating.chgk.info/teams/49804)**
- Дмитрий Сахаров
- Руслан Хаиткулов
- Сергей Спешков
- Иван Семушин
- Алексей Андрюшин

Второе место заняла команда [«Я просто медленно пишу»](https://rating.chgk.info/teams/71595) (Москва), третье — [«Дальше уже»](https://rating.chgk.info/teams/52143) (Екатеринбург).

Полные результаты можно найти [на этой странице](https://dope.pecheny.me/fest/chr2026/game/ek/). Больше информации о турнире — [в этом телеграм-канале](https://t.me/ruchamp_intgames/251) и [здесь](https://t.me/chgknews/1176).

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ksi"></div>

<a id="game-ksi"></a>

- [II ЧР по командной «Своей игре» (2026)](#ksi_2026)
- [I ЧР по командной «Своей игре» (2025)](#ksi_2025)


**II ЧР по командной «Своей игре»** прошёл 13 июня 2026 года в Москве. <a name="ksi_2026"></a>

Победитель: **[«Борский корабел» (Москва)](https://rating.chgk.info/teams/49804)**
- Дмитрий Сахаров
- Руслан Хаиткулов
- Сергей Спешков
- Иван Семушин
- Алексей Андрюшин

Второе место заняла команда [«Рабочее название»](https://rating.chgk.info/teams/45556) (Санкт-Петербург), третье — [«ff»](https://rating.chgk.info/teams/45470) (Москва).

Полные результаты можно найти [на этой странице](https://dope.pecheny.me/fest/chr2026/game/ksi/#results). Больше информации о турнире — [в этом телеграм-канале](https://t.me/ruchamp_intgames/251) и [здесь](https://t.me/chgknews/1176).

---

**I ЧР по командной «Своей игре»** прошёл 13 июня 2025 года в Москве. <a name="ksi_2025"></a>

Победитель: **[«Рабочее название» (Санкт-Петербург)](https://rating.chgk.info/teams/45556)**
- Юрий Выменец
- Сергей Евсеев
- Сергей Коновалов
- Александр Либер
- Сергей Николенко
- Ирина Прокофьева
- Вадим Раскумандрин
- Сергей Шеремет

Второе место заняла команда [«София»](https://rating.chgk.info/teams/45174) (Саранск), третье — [«Призраки Коши»](https://rating.chgk.info/teams/27177) (Санкт-Петербург).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1qs9hVN3FGheWolq96-6zixSnAP6bi53HLNDd-pPTC2Y/edit?gid=896277444#gid=896277444). Больше информации о турнире — [в этом телеграм-канале](https://t.me/ruchamp_intgames/108) и [здесь](https://t.me/chgknews/1487).

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-kvrm"></div>

<a id="game-kvrm"></a>

- [II ЧР по КВРМ (2026)](#kvrm_2026)
- [I ЧР по КВРМ (2025)](#kvrm_2025)


**II ЧР по КВРМ** прошёл 13–14 июня 2026 года в Москве. <a name="kvrm_2026"></a>

Победитель: **[«Борский корабел» (Москва)](https://rating.chgk.info/teams/49804)**
- Дмитрий Сахаров
- Руслан Хаиткулов
- Сергей Спешков
- Иван Семушин
- Максим Руссо
- Александра Брутер

Второе место заняла команда [«Призраки Коши»](https://rating.chgk.info/teams/27177) (Санкт-Петербург), третье — [«Тихие Тигры»](https://rating.chgk.info/teams/75592) (Мытищи).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12826), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/6900). Больше информации о турнире — [в этом телеграм-канале](https://t.me/ruchamp_intgames/251) и [здесь](https://t.me/chgknews/1176).

---

**I ЧР по КВРМ** прошёл 13–14 июня 2025 года в Москве. <a name="kvrm_2025"></a>

Победитель: **[«Борский корабел» (Москва)](https://rating.chgk.info/teams/49804)**
- Дмитрий Сахаров
- Руслан Хаиткулов
- Сергей Спешков
- Иван Семушин
- Максим Руссо
- Александра Брутер

Второе место заняла команда [«Первая сборная»](https://rating.chgk.info/teams/4109) (Москва), третье — [«Рождённый с ПТСР»](https://rating.chgk.info/teams/103505) (Раменское).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11749), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/6369). Больше информации о турнире — [в этом телеграм-канале](https://t.me/ruchamp_intgames/108) и [здесь](https://t.me/chgknews/1487).

---

<div class="country-tab-end"></div>
