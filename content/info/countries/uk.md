---
title: Великобритания
weight: 1
bookToC: false
---

# Великобритания

Чемпионаты Великобритании проводятся с 2008 года.

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-chgk" aria-selected="false">Турниры по ЧГК</button><button type="button" role="tab" data-tab="game-ssi" aria-selected="false">Турниры по ССИ</button><button type="button" role="tab" data-tab="missing-data" aria-selected="false">Проблемы</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th>Команда</th><th>Город</th><th>I</th><th>II</th><th>III</th><th>∑</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/5397">Ворона и Медведы (SteamPug)</a></td>
<td>Лондон</td>
<td>1</td>
<td>4</td>
<td>5</td>
<td>10</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/5086">Стрела</a></td>
<td>Лондон</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/43876">Сова нашла хвост</a></td>
<td>Лондон</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/4730">Greedy Squirrel</a></td>
<td>Лондон</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/79988">Капибара мордой вниз (Совет в Финчлях / Опекают Капибар / Прикапибарилось)</a></td>
<td>Лондон</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/48869">2,5 человека</a></td>
<td>Лондон</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/6651">А5 (Жрецы Хамона)</a></td>
<td>Лондон</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/98778">Council faces the wrath of the tulip grove defenders (Badger admiring art / Tulip grove defenders)</a></td>
<td>сборная</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/58375">Стэнфордский эксперимент</a></td>
<td>Стэнфорд</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/98414">Acquired Taste</a></td>
<td>Лондон</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/39258">Британские учёные</a></td>
<td>Кембридж</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/56561">6 жён Генриха 8</a></td>
<td>Лондон</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/44305">Апельсиновые учёные</a></td>
<td>Кембридж</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/935">Глюки</a></td>
<td>Рига</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/46828">Мохнатые учёные</a></td>
<td>Лондон</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/48801">Овечка Долли</a></td>
<td>Эдинбург</td>
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
<td><a href="https://rating.chgk.info/player/21235">Ирина Михлина</a></td>
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
<td><a href="https://rating.chgk.info/player/1613">Дмитрий Арш</a></td>
<td>6</td>
<td>3</td>
<td>1</td>
<td>10</td>
<td>6</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21234">Леонид Михлин</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2031">Тогрул Багиров</a></td>
<td>1</td>
<td>4</td>
<td>5</td>
<td>10</td>
<td>1</td>
<td>4</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21428">Вадим Молдавский</a></td>
<td>5</td>
<td>3</td>
<td>1</td>
<td>9</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18688">Галина Локшина</a></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>9</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29787">Татьяна Снеговская-Арш</a></td>
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
<td><a href="https://rating.chgk.info/player/23367">Борис Окунь</a></td>
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
<td><a href="https://rating.chgk.info/player/33239">Софья Окунь</a></td>
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
<td><a href="https://rating.chgk.info/player/22896">Алексей Новаков</a></td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>7</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26801">Ольга Резницкая</a></td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>7</td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18540">Константин Лихоманов</a></td>
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
<td><a href="https://rating.chgk.info/player/2917">Дмитрий Белицкий</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36387">Константин Шлыков</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11466">Евгений Затуловский</a></td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>6</td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8835">Анна Казарновская</a></td>
<td>0</td>
<td>2</td>
<td>4</td>
<td>6</td>
<td>0</td>
<td>2</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2853">Вадим Бейлин</a></td>
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
<td><a href="https://rating.chgk.info/player/2547">Дмитрий Барский</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2545">Светлана Барская</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11627">Андрей Зеленеев</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29943">Ирина Соколова</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/42945">Никита Иоффе</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6794">Альберт Геворкян</a></td>
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
<td><a href="https://rating.chgk.info/player/66736">Антон Гуревич</a></td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>5</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7604">Евгений Горбатиков</a></td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>5</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7177">Виктор Глухов</a></td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>4</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71033">Анастасия Гордеева</a></td>
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
<td><a href="https://rating.chgk.info/player/13475">Илья Карасик</a></td>
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
<td><a href="https://rating.chgk.info/player/28302">Валерий Сатыбалдыев</a></td>
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
<td><a href="https://rating.chgk.info/player/29428">Виолетта Скрипникова</a></td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/72498">Алёна Тарасова</a></td>
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
<td><a href="https://rating.chgk.info/player/122937">Илья Гончаров</a></td>
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
<td><a href="https://rating.chgk.info/player/5555">Наталья Викулина</a></td>
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
<td><a href="https://rating.chgk.info/player/66403">Виталий Бреев</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/65051">Денис Рубцов</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71907">Елизавета Короткова</a></td>
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
<td><a href="https://rating.chgk.info/player/77673">Михаил Папков</a></td>
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
<td><a href="https://rating.chgk.info/player/33943">Гайк Хемчян</a></td>
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
<td><a href="https://rating.chgk.info/player/7861">Максим Горюнов</a></td>
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
<td><a href="https://rating.chgk.info/player/63331">Дарья Овсянникова</a></td>
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
<td><a href="https://rating.chgk.info/player/188961">Дмитрий Матов</a></td>
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
<td><a href="https://rating.chgk.info/player/75296">Александра Генкина</a></td>
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
<td><a href="https://rating.chgk.info/player/63334">Анна Нужная</a></td>
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
<td><a href="https://rating.chgk.info/player/2033">Вардан Багирян</a></td>
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
<td><a href="https://rating.chgk.info/player/30460">Дмитрий Степаненко</a></td>
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
<td><a href="https://rating.chgk.info/player/75297">Илларион Бейсембаев</a></td>
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
<td><a href="https://rating.chgk.info/player/27013">Ирина Рожко</a></td>
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
<td><a href="https://rating.chgk.info/player/69720">Максим Галкин</a></td>
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
<td><a href="https://rating.chgk.info/player/83268">Мария Тимохова</a></td>
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
<td><a href="https://rating.chgk.info/player/18132">Николай Лёгенький</a></td>
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
<td><a href="https://rating.chgk.info/player/25607">Сергей Пономарёв</a></td>
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
<td><a href="https://rating.chgk.info/player/86903">Анастасия Максимовских</a></td>
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
<td><a href="https://rating.chgk.info/player/194916">Андрей Колосов</a></td>
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
<td><a href="https://rating.chgk.info/player/12469">Ирина Изместьева</a></td>
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
<td><a href="https://rating.chgk.info/player/18517">Ирина Литовченко</a></td>
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
<td><a href="https://rating.chgk.info/player/95648">Лидия Колесниченко</a></td>
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
<td><a href="https://rating.chgk.info/player/140465">Михаил Пенкин</a></td>
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
<td><a href="https://rating.chgk.info/player/19428">Николай Максимов</a></td>
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
<td><a href="https://rating.chgk.info/player/74520">Михаил Карташов</a></td>
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
<td><a href="https://rating.chgk.info/player/40044">Мишель Гассиб</a></td>
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
<td><a href="https://rating.chgk.info/player/84198">Станислав Завьялов</a></td>
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
<td><a href="https://rating.chgk.info/player/35962">Алина Шелег</a></td>
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
<td><a href="https://rating.chgk.info/player/29896">Василий Соколов</a></td>
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
<td><a href="https://rating.chgk.info/player/72479">Кирилл Карташов</a></td>
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
<td><a href="https://rating.chgk.info/player/32253">Никита Труханов</a></td>
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
<td><a href="https://rating.chgk.info/player/7666">Сергей Горбунов</a></td>
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
<td><a href="https://rating.chgk.info/player/26911">Александр Фингеров</a></td>
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
<td><a href="https://rating.chgk.info/player/34958">Алиса Чернявская</a></td>
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
<td><a href="https://rating.chgk.info/player/54136">Амаль Имангулов</a></td>
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
<td><a href="https://rating.chgk.info/player/28255">Ваган Сардарян</a></td>
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
<td><a href="https://rating.chgk.info/player/20072">Карен Марутян</a></td>
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
<td><a href="https://rating.chgk.info/player/146376">Майя Полищук</a></td>
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
<td><a href="https://rating.chgk.info/player/62939">Александр Шишов</a></td>
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
<td><a href="https://rating.chgk.info/player/74078">Алексей Попель</a></td>
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
<td><a href="https://rating.chgk.info/player/5185">Анастасия Васильченкова</a></td>
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
<td><a href="https://rating.chgk.info/player/45151">Андрей Гусев</a></td>
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
<td><a href="https://rating.chgk.info/player/26037">Анна Прищепа</a></td>
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
<td><a href="https://rating.chgk.info/player/84199">Антон Гинель</a></td>
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
<td><a href="https://rating.chgk.info/player/67304">Антон Малютин</a></td>
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
<td><a href="https://rating.chgk.info/player/25333">Антон Поздняков</a></td>
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
<td><a href="https://rating.chgk.info/player/12656">Виктор Исаев</a></td>
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
<td><a href="https://rating.chgk.info/player/20271">Виктор Матросов</a></td>
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
<td><a href="https://rating.chgk.info/player/22281">Виктор Народицкий</a></td>
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
<td><a href="https://rating.chgk.info/player/21807">Дмитрий Мунда</a></td>
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
<td><a href="https://rating.chgk.info/player/2319">Евгений Балкинд</a></td>
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
<td><a href="https://rating.chgk.info/player/73589">Евгений Савченко</a></td>
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
<td><a href="https://rating.chgk.info/player/181810">Евгения Фёдорова</a></td>
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
<td><a href="https://rating.chgk.info/player/40324">Елена Михайлова</a></td>
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
<td><a href="https://rating.chgk.info/player/13523">Игорь Карзов</a></td>
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
<td><a href="https://rating.chgk.info/player/152976">Игорь Козлов</a></td>
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
<td><a href="https://rating.chgk.info/player/31682">Илона Тинтс</a></td>
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
<td><a href="https://rating.chgk.info/player/23459">Ирина Нургалеева</a></td>
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
<td><a href="https://rating.chgk.info/player/74536">Марина Ломберг</a></td>
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
<td><a href="https://rating.chgk.info/player/20278">Ольга Матросова</a></td>
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
<td><a href="https://rating.chgk.info/player/23294">Руслан Огородник</a></td>
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
<td><a href="https://rating.chgk.info/player/139801">Тигран Нагапетян</a></td>
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
<td><a href="https://rating.chgk.info/player/74523">Фарадж Халили</a></td>
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
<td><a href="https://rating.chgk.info/player/35385">Эдуард Шагал</a></td>
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
<td><a href="https://rating.chgk.info/player/89279">Эльмира Раджабли</a></td>
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
<td><a href="https://rating.chgk.info/player/16053">Александр Котенко</a></td>
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
<td><a href="https://rating.chgk.info/player/37436">Александра Ярцева</a></td>
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
<td><a href="https://rating.chgk.info/player/23461">Анна Билас</a></td>
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
<td><a href="https://rating.chgk.info/player/162332">Анна Малютина</a></td>
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
<td><a href="https://rating.chgk.info/player/67154">Влада Корсунская</a></td>
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
<td><a href="https://rating.chgk.info/player/24226">Дарья Парузина</a></td>
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
<td><a href="https://rating.chgk.info/player/117755">Дарья Платонова</a></td>
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
<td><a href="https://rating.chgk.info/player/3381">Денис Билас</a></td>
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
<td><a href="https://rating.chgk.info/player/46766">Дмитрий Макаров</a></td>
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
<td><a href="https://rating.chgk.info/player/88162">Екатерина Марышева</a></td>
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
<td><a href="https://rating.chgk.info/player/20119">Иван Марышев</a></td>
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
<td><a href="https://rating.chgk.info/player/65078">Иван Тебляшкин</a></td>
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
<td><a href="https://rating.chgk.info/player/19231">Максим Майданский</a></td>
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
<td><a href="https://rating.chgk.info/player/52670">Мария Макарова</a></td>
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
<td><a href="https://rating.chgk.info/player/21158">Мария Михайлова</a></td>
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
<td><a href="https://rating.chgk.info/player/21159">Наталия Михайлова</a></td>
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
<td><a href="https://rating.chgk.info/player/63332">Наталья Булгакова</a></td>
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
<td><a href="https://rating.chgk.info/player/21855">Николай Мурашкин</a></td>
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
<td><a href="https://rating.chgk.info/player/3309">Павел Бессонов</a></td>
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
<td><a href="https://rating.chgk.info/player/65893">Сэсэгма Санжиева</a></td>
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
<td><a href="https://rating.chgk.info/player/61835">Юлия Корчагина</a></td>
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

- [XVIII чемпионат Великобритании по спортивному ЧГК (2026)](#chgk_2026)
- [XVII чемпионат Великобритании по спортивному ЧГК (2025)](#chgk_2025)
- [XVI чемпионат Великобритании по спортивному ЧГК (2024)](#chgk_2024)
- [XV чемпионат Великобритании по спортивному ЧГК (2023)](#chgk_2023)
- [XIV чемпионат Великобритании по спортивному ЧГК (2022)](#chgk_2022)
- [XIII чемпионат Великобритании по спортивному ЧГК (2021)](#chgk_2021)
- [XII чемпионат Великобритании по спортивному ЧГК (2019)](#chgk_2019)
- [XI чемпионат Великобритании по спортивному ЧГК (2018)](#chgk_2018)
- [X чемпионат Великобритании по спортивному ЧГК (2017)](#chgk_2017)
- [IX чемпионат Великобритании по спортивному ЧГК (2016)](#chgk_2016)
- [VIII чемпионат Великобритании по спортивному ЧГК (2015)](#chgk_2015)
- [VII чемпионат Великобритании по спортивному ЧГК (2014)](#chgk_2014)
- [VI чемпионат Великобритании по спортивному ЧГК (2013)](#chgk_2013)
- [V чемпионат Великобритании по спортивному ЧГК (2012)](#chgk_2012)
- [IV чемпионат Великобритании по спортивному ЧГК (2011)](#chgk_2011)
- [III чемпионат Великобритании по спортивному ЧГК (2010)](#chgk_2010)
- [II чемпионат Великобритании по спортивному ЧГК (2009)](#chgk_2009)
- [I чемпионат Великобритании по спортивному ЧГК (2008)](#chgk_2008)


**XVIII чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 16–17 мая 2026 года в Лондоне. <a id="chgk_2026"></a>

Победитель: **[Tulip grove defenders (сборная)](https://rating.chgk.info/teams/98778)**
- Михаил Папков
- Елизавета Короткова
- Амаль Имангулов
- Александр Фингеров
- Вадим Молдавский
- Николай Максимов

Второе место заняла команда [«2,5 человека»](https://rating.chgk.info/teams/48869) (Лондон), третье — [Acquired Taste](https://rating.chgk.info/teams/98414) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/13612).

*[К оглавлению](#chgk_contents)*

---

**XVII чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 17–18 мая 2025 года в Лондоне. <a id="chgk_2025"></a>

Победитель: **[Acquired Taste (Лондон)](https://rating.chgk.info/teams/98414)**
- Андрей Колосов
- Михаил Пенкин
- Лидия Колесниченко
- Анастасия Максимовских
- Анастасия Гордеева
- Максим Горюнов

Второе место заняла команда [«Совет в Финчлях»](https://rating.chgk.info/teams/79988) (Лондон), третье — [Badger admiring art](https://rating.chgk.info/teams/98778) (сборная).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11919).

*[К оглавлению](#chgk_contents)*

---

**XVI чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 4 мая 2024 года в Лондоне. <a id="chgk_2024"></a>

Победитель: **[«Прикапибарилось» (Лондон)](https://rating.chgk.info/teams/79988)**
- Никита Иоффе
- Софья Окунь
- Ирина Соколова
- Борис Окунь
- Константин Лихоманов
- Николай Лёгенький
- Андрей Зеленеев

Второе место заняла команда [Council faces the wrath of the tulip grove defenders](https://rating.chgk.info/teams/98778) (сборная), третье — [«2,5 человека»](https://rating.chgk.info/teams/48869) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/10237).

*[К оглавлению](#chgk_contents)*

---

**XV чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 27 мая 2023 года в Кембридже. <a id="chgk_2023"></a>

Победитель: **[«Опекают Капибар» (Лондон)](https://rating.chgk.info/teams/79988)**
- Никита Иоффе
- Софья Окунь
- Ирина Соколова
- Борис Окунь
- Константин Лихоманов
- Андрей Зеленеев

Второе место разделили команды [SteamPug](https://rating.chgk.info/teams/5397) (Лондон) и [«2,5 человека»](https://rating.chgk.info/teams/48869) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/9038).

*[К оглавлению](#chgk_contents)*

---

**XIV чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 21 мая 2022 года в Кембридже. <a id="chgk_2022"></a>

Победитель: **[«Стэнфордский эксперимент» (Стэнфорд)](https://rating.chgk.info/teams/58375)**
- Максим Галкин
- Денис Рубцов
- Ваган Сардарян
- Карен Марутян
- Евгений Затуловский
- Вардан Багирян

Второе место заняла команда [«Жрецы Хамона»](https://rating.chgk.info/teams/6651) (Лондон), третье — [«Совет в Финчлях»](https://rating.chgk.info/teams/79988) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/7805).

*[К оглавлению](#chgk_contents)*

---

**XIII чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 11 сентября 2021 года в Лондоне. <a id="chgk_2021"></a>

Победитель: **[«2,5 человека» (Лондон)](https://rating.chgk.info/teams/48869)**
- Илларион Бейсембаев
- Александра Генкина
- Антон Гуревич
- Валерий Сатыбалдыев
- Сергей Пономарёв
- Евгений Горбатиков

Второе место заняла команда [«Капибара мордой вниз»](https://rating.chgk.info/teams/79988) (Лондон), третье — [«Ворона и Медведы»](https://rating.chgk.info/teams/5397) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/6114).

*[К оглавлению](#chgk_contents)*

---

**XII чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 5 мая 2019 года в Лондоне. <a id="chgk_2019"></a>

Победитель: **[«Жрецы Хамона» (Лондон)](https://rating.chgk.info/teams/6651)**
- Илья Гончаров
- Алёна Тарасова
- Анастасия Гордеева
- Софья Окунь
- Борис Окунь
- Константин Лихоманов

Второе место заняла команда [«6 жён Генриха 8»](https://rating.chgk.info/teams/56561) (Лондон), третье — [«Ворона и Медведы»](https://rating.chgk.info/teams/5397) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5448).

*[К оглавлению](#chgk_contents)*

---

**XI чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 14 апреля 2018 года в Кембридже. <a id="chgk_2018"></a>

Победитель: **[«Жрецы Хамона» (Лондон)](https://rating.chgk.info/teams/6651)**
- Илья Гончаров
- Мария Тимохова
- Алёна Тарасова
- Софья Окунь
- Дмитрий Степаненко
- Борис Окунь

Второе место разделили команды [«Ворона и Медведы»](https://rating.chgk.info/teams/5397) (Лондон) и [«Стэнфордский эксперимент»](https://rating.chgk.info/teams/58375) (Стэнфорд).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4856).

*[К оглавлению](#chgk_contents)*

---

**X чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 9 апреля 2017 года в Кембридже. <a id="chgk_2017"></a>

Победитель: **[«Сова нашла хвост» (Лондон)](https://rating.chgk.info/teams/43876)**
- Майя Полищук
- Алиса Чернявская
- Татьяна Снеговская-Арш
- Вадим Молдавский
- Вадим Бейлин
- Дмитрий Арш

Второе место разделили команды [«Ворона и Медведы»](https://rating.chgk.info/teams/5397) (Лондон) и [«2,5 человека»](https://rating.chgk.info/teams/48869) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4255).

*[К оглавлению](#chgk_contents)*

---

**IX чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 22 мая 2016 года в Лондоне. <a id="chgk_2016"></a>

Победитель: **[«Сова нашла хвост» (Лондон)](https://rating.chgk.info/teams/43876)**
- Виталий Бреев
- Татьяна Снеговская-Арш
- Вадим Молдавский
- Виктор Глухов
- Вадим Бейлин
- Дмитрий Арш

Второе место заняла команда [«Ворона и Медведы»](https://rating.chgk.info/teams/5397) (Лондон), третье — [«Стрела»](https://rating.chgk.info/teams/5086) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3797).

*[К оглавлению](#chgk_contents)*

---

**VIII чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 29 марта 2015 года в Лондоне. <a id="chgk_2015"></a>

Победитель: **[«Ворона и Медведы» (Лондон)](https://rating.chgk.info/teams/5397)**
- Гайк Хемчян
- Ольга Резницкая
- Алексей Новаков
- Ирина Михлина
- Леонид Михлин
- Галина Локшина
- Тогрул Багиров

Второе место заняла команда [«Сова нашла хвост»](https://rating.chgk.info/teams/43876) (Лондон), третье — [«Овечка Долли»](https://rating.chgk.info/teams/48801) (Эдинбург).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3214).

*[К оглавлению](#chgk_contents)*

---

**VII чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 16 марта 2014 года в Лондоне. <a id="chgk_2014"></a>

Победитель: **[«Сова нашла хвост» (Лондон)](https://rating.chgk.info/teams/43876)**
- Татьяна Снеговская-Арш
- Вадим Молдавский
- Виктор Глухов
- Наталья Викулина
- Вадим Бейлин
- Дмитрий Арш

Второе место заняла команда [«Мохнатые учёные»](https://rating.chgk.info/teams/46828) (Лондон), третье — [«Ворона и Медведы»](https://rating.chgk.info/teams/5397) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2823).

*[К оглавлению](#chgk_contents)*

---

**VI чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 21 апреля 2013 года в Лондоне. <a id="chgk_2013"></a>

Победитель: **[«Сова нашла хвост» (Лондон)](https://rating.chgk.info/teams/43876)**
- Татьяна Снеговская-Арш
- Вадим Молдавский
- Виктор Глухов
- Наталья Викулина
- Вадим Бейлин
- Дмитрий Арш

Второе место заняла команда [«Апельсиновые учёные»](https://rating.chgk.info/teams/44305) (Кембридж), третье — [«Ворона и Медведы»](https://rating.chgk.info/teams/5397) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2347).

*[К оглавлению](#chgk_contents)*

---

**V чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 28 апреля 2012 года в Лондоне. <a id="chgk_2012"></a>

Победитель: **[Greedy Squirrel (Лондон)](https://rating.chgk.info/teams/4730)**
- Ирина Михлина
- Леонид Михлин
- Дмитрий Барский
- Светлана Барская

Второе место разделили команды [«Стрела»](https://rating.chgk.info/teams/5086) (Лондон) и [«Британские учёные»](https://rating.chgk.info/teams/39258) (Кембридж).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2091).

*[К оглавлению](#chgk_contents)*

---

**IV чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 22 мая 2011 года в Лондоне. <a id="chgk_2011"></a>

Победитель: **[«Стрела» (Лондон)](https://rating.chgk.info/teams/5086)**
- Анна Нужная
- Константин Шлыков
- Ирина Рожко
- Илья Карасик
- Альберт Геворкян
- Дмитрий Белицкий

Второе место заняла команда [Greedy Squirrel](https://rating.chgk.info/teams/4730) (Лондон), третье — [«Британские учёные»](https://rating.chgk.info/teams/39258) (Кембридж).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1821).

*[К оглавлению](#chgk_contents)*

---

**III чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 24 апреля 2010 года в Лондоне. <a id="chgk_2010"></a>

Победитель: **[Greedy Squirrel (Лондон)](https://rating.chgk.info/teams/4730)**
- Татьяна Снеговская-Арш
- Ирина Михлина
- Леонид Михлин
- Дмитрий Барский
- Светлана Барская
- Дмитрий Арш

Второе место заняла команда [«Стрела»](https://rating.chgk.info/teams/5086) (Лондон), третье — [«А5»](https://rating.chgk.info/teams/6651) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/619).

*[К оглавлению](#chgk_contents)*

---

**II чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 27 марта 2009 года в Лондоне. <a id="chgk_2009"></a>

Победитель: **[«Стрела» (Лондон)](https://rating.chgk.info/teams/5086)**
- Константин Шлыков
- Ирина Литовченко
- Илья Карасик
- Ирина Изместьева
- Альберт Геворкян
- Дмитрий Белицкий

Второе место заняла команда [Greedy Squirrel](https://rating.chgk.info/teams/4730) (Лондон), третье — [«Ворона и Медведы»](https://rating.chgk.info/teams/5397) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/444).

*[К оглавлению](#chgk_contents)*

---

**I чемпионат Великобритании по спортивному «Что? Где? Когда?»** прошёл 27 апреля 2008 года в Лондоне. <a id="chgk_2008"></a>

Победитель: **[Greedy Squirrel (Лондон)](https://rating.chgk.info/teams/4730)**
- Татьяна Снеговская-Арш
- Ирина Михлина
- Леонид Михлин
- Дмитрий Барский
- Светлана Барская
- Дмитрий Арш

Второе место заняла команда [«Глюки»](https://rating.chgk.info/teams/935) (Рига), третье — [«Стрела»](https://rating.chgk.info/teams/5086) (Лондон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/333).

*[К оглавлению](#chgk_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ssi"></div>

<a id="game-ssi"></a><a id="ssi_contents" name="ssi_contents"></a>

- [I чемпионат Великобритании по ССИ (2014)](#ssi_2014)


**I чемпионат Великобритании по спортивной «Своей игре»** прошёл 15 марта 2014 года в Лондоне. <a id="ssi_2014"></a>

Победитель: **[Виталий Бреев](https://rating.chgk.info/player/66403)**

Второе место занял [Вадим Молдавский](https://rating.chgk.info/player/21428), третье — [Дмитрий Арш](https://rating.chgk.info/player/1613).

Полные результаты можно найти [на этой странице](https://chgk-uk.livejournal.com/2014/03/15/). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20150513204156/http://london.chgk.info/tournaments/chuk/2014).

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
<tr><td>2023</td><td><a href="https://rating.chgk.info/tournament/9038">XV чемпионат Великобритании по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2018</td><td><a href="https://rating.chgk.info/tournament/4856">XI чемпионат Великобритании по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2017</td><td><a href="https://rating.chgk.info/tournament/4255">X чемпионат Великобритании по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2012</td><td><a href="https://rating.chgk.info/tournament/2091">V чемпионат Великобритании по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
