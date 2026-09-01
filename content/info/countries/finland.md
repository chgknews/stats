---
title: Финляндия
weight: 1
bookToC: false
---

# Финляндия

Чемпионаты Финляндии проводятся с 2004 года.

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-chgk" aria-selected="false">Чемпионаты</button><button type="button" role="tab" data-tab="missing-data" aria-selected="false">Нет данных</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th>Команда</th><th>Город</th><th>I</th><th>II</th><th>III</th><th>∑</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/42483">Пахом Пихай</a></td>
<td>Хельсинки</td>
<td>10</td>
<td>1</td>
<td>0</td>
<td>11</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3950">Мы-6</a></td>
<td>Хельсинки</td>
<td>3</td>
<td>7</td>
<td>1</td>
<td>11</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/133">Дети капитана Врунгеля</a></td>
<td>Хельсинки</td>
<td>0</td>
<td>6</td>
<td>2</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3521">777</a></td>
<td>Хельсинки</td>
<td>2</td>
<td>3</td>
<td>2</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/129">Эмси-Эмси</a></td>
<td>Хельсинки</td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/132">Седьмой этаж</a></td>
<td>Хельсинки</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/130">Столичные лобстеры</a></td>
<td>Эспоо</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3522">Primus inter pares</a></td>
<td>Хельсинки</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/91946">Пробковый ноктурлабиум</a></td>
<td>Хельсинки</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/131">Склочные пузырьки</a></td>
<td>Хельсинки</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/41538">Кира Корпи</a></td>
<td>Хельсинки</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/58400">Один и Пустота</a></td>
<td>Хельсинки</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/50821">Собакусъел</a></td>
<td>Санкт-Петербург</td>
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
<tr><th>Игрок</th><th>I</th><th>II</th><th>III</th><th>∑</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/player/4730">Владислав Быков</a></td>
<td>11</td>
<td>3</td>
<td>1</td>
<td>15</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9188">Ольга Деркач</a></td>
<td>11</td>
<td>3</td>
<td>1</td>
<td>15</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5720">Иван Власов</a></td>
<td>2</td>
<td>8</td>
<td>3</td>
<td>13</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12474">Константин Изъюров</a></td>
<td>10</td>
<td>1</td>
<td>0</td>
<td>11</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/16561">Александр Кротов</a></td>
<td>2</td>
<td>7</td>
<td>1</td>
<td>10</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13745">Екатерина Катаева</a></td>
<td>2</td>
<td>7</td>
<td>1</td>
<td>10</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35270">Вадим Чупасов</a></td>
<td>2</td>
<td>6</td>
<td>1</td>
<td>9</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/16329">Ксения Шагал</a></td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35385">Эдуард Шагал</a></td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6216">Алексей Выскубов</a></td>
<td>2</td>
<td>3</td>
<td>2</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5732">Анастасия Власова</a></td>
<td>2</td>
<td>3</td>
<td>2</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34309">Светлана Хяннинен</a></td>
<td>2</td>
<td>3</td>
<td>2</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13292">Александр Каневский</a></td>
<td>2</td>
<td>2</td>
<td>3</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/61762">Михаил Пярнянен</a></td>
<td>0</td>
<td>6</td>
<td>1</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1641">Владимир Асеев</a></td>
<td>0</td>
<td>5</td>
<td>2</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32041">Лилия Тоссавайнен</a></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/104117">Алина Ильинская</a></td>
<td>0</td>
<td>5</td>
<td>1</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18605">Елена Лобынцева</a></td>
<td>0</td>
<td>4</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32356">Павел Тупин</a></td>
<td>0</td>
<td>4</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5431">Анатолий Верховский</a></td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/75249">Марина Шубина</a></td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/75248">Михаил Шубин</a></td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7008">Алексей Гилёв</a></td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3960">Александр Борисов</a></td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12807">Владимир Ищенко</a></td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9719">Виктор Древицкий</a></td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19274">Наталья Макаренко</a></td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30918">Руслан Суси</a></td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3986">Алла Борисова</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1608">Денис Арчаков</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19757">София Линдберг</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/47184">Тойво Тупин</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7056">Дмитрий Гиренко</a></td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33558">Дмитрий Фурсов</a></td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2904">Илья Белевич</a></td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27874">Юсиф Садыхов</a></td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29017">Алексей Сидоров</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7037">Евгений Гимер</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31377">Леван Твалтвадзе</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8321">Евгений Грязин</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23811">Михаил Павельев</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54273">Павел Алексейчик</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/61761">Александр Грабовский</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/79737">Варвара Шумова</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30161">Александр Сорокин</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/145111">Алексей Пак</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/243260">Владислав Баканов</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/256410">Михаил Циплев</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34391">Тимофей Целых</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/24434">Артур Пенттинен</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31756">Мария Пенттинен</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2652">Алексей Батов</a></td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/147292">Виктория Батанова</a></td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2920">Олег Белецкий</a></td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22120">Максим Нагорнов</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37541">Максим Беспалов</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28557">Юрий Сейгер</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/418">Алексей Адамов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31753">Алёна Вялья</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/134420">Анна Пивоварова</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21931">Арсений Мустафин</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/151317">Константин Баранников</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/288254">Александр Сагаловский</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9586">Андрей Доманский</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35875">Андрей Шевченко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13145">Анна Калинчук</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21842">Артур Муратов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/334004">Вусал Гусейнов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/139605">Диана Черниченко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/63402">Екатерина Хювяринен</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17251">Константин Куличихин</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18794">Михаил Лубченков</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33561">Надежда Фурсова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9587">Николай Доманский</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28412">Ольга Сванберг</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/329005">Юлия Атласова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19400">Ян Макохагон</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/79675">Александр Бережной</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/246051">Александр Левенцов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/111938">Анастасия Дробышева</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31351">Андрей Таубер</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/72267">Виктория Петровская</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/136">Георгий Абрамов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/113943">Елена Мельник</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/99931">Елена Холмгрен</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1325">Ирина Анурова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/61763">Ирина Кантонистова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/186366">Ксения Табакова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/72265">Максим Фёдоров</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/91143">Михаил Васильев</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5302">Ольга Вековищева</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/130041">Павел Пономарёв</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/114187">Роман Пак</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28493">Сергей Севастьянов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36385">Сергей Шлихунов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15715">Ярослав Корнилов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-chgk"></div>

<a id="game-chgk"></a><a name="contents"></a>

- [XX чемпионат Финляндии по спортивному ЧГК (2026)](#chgk_2026)
- [XIX чемпионат Финляндии по спортивному ЧГК (2025)](#chgk_2025)
- [XVIII чемпионат Финляндии по спортивному ЧГК (2024)](#chgk_2024)
- [XVII чемпионат Финляндии по спортивному ЧГК (2023)](#chgk_2023)
- [XVI чемпионат Финляндии по спортивному ЧГК (2019)](#chgk_2019)
- [XV чемпионат Финляндии по спортивному ЧГК (2018)](#chgk_2018)
- [XIV чемпионат Финляндии по спортивному ЧГК (2017)](#chgk_2017)
- [XIII чемпионат Финляндии по спортивному ЧГК (2016)](#chgk_2016)
- [XII чемпионат Финляндии по спортивному ЧГК (2015)](#chgk_2015)
- [XI чемпионат Финляндии по спортивному ЧГК (2014)](#chgk_2014)
- [X чемпионат Финляндии по спортивному ЧГК (2013)](#chgk_2013)
- [IX чемпионат Финляндии по спортивному ЧГК (2012)](#chgk_2012)
- [VIII чемпионат Финляндии по спортивному ЧГК (2011)](#chgk_2011)
- [VII чемпионат Финляндии по спортивному ЧГК (2010)](#chgk_2010)
- [VI чемпионат Финляндии по спортивному ЧГК (2009)](#chgk_2009)
- [V чемпионат Финляндии по спортивному ЧГК (2008)](#chgk_2008)
- [IV чемпионат Финляндии по спортивному ЧГК (2007)](#chgk_2007)
- [III чемпионат Финляндии по спортивному ЧГК (2006)](#chgk_2006)
- [II чемпионат Финляндии по спортивному ЧГК (2005)](#chgk_2005)
- [I чемпионат Финляндии по спортивному ЧГК (2004)](#chgk_2004)


**XX чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 16 мая 2026 года в Хельсинки. <a name="chgk_2026"></a>

Победитель: **[«Пробковый ноктурлабиум» (Хельсинки)](https://rating.chgk.info/teams/91946)**
- Михаил Циплев
- Владислав Баканов
- Константин Баранников
- Алексей Пак
- Анна Пивоварова
- Арсений Мустафин

Второе место заняла команда [«Пахом Пихай»](https://rating.chgk.info/teams/42483) (Хельсинки), третье — [«Мы-6»](https://rating.chgk.info/teams/3950) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/13759).


*[К оглавлению](#contents)*

---

**XIX чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 17 мая 2025 года в Хельсинки. <a name="chgk_2025"></a>

Победитель: **[«Пахом Пихай» (Хельсинки)](https://rating.chgk.info/teams/42483)**
- Константин Изъюров
- Ольга Деркач
- Алексей Гилёв
- Владислав Быков

Второе место разделили команды [«Мы-6»](https://rating.chgk.info/teams/3950) (Хельсинки) и [«Пробковый ноктурлабиум»](https://rating.chgk.info/teams/91946) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12186).


*[К оглавлению](#contents)*

---

**XVIII чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 25 мая 2024 года в Хельсинки. <a name="chgk_2024"></a>

Победитель: **[«Пахом Пихай» (Хельсинки)](https://rating.chgk.info/teams/42483)**
- Константин Изъюров
- Ольга Деркач
- Алексей Гилёв
- Владислав Быков

Второе место заняла команда [«Эмси-Эмси»](https://rating.chgk.info/teams/129) (Хельсинки), третье — [«Собакусъел»](https://rating.chgk.info/teams/50821) (Санкт-Петербург).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11375).


*[К оглавлению](#contents)*

---

**XVII чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 20 мая 2023 года в Хельсинки. <a name="chgk_2023"></a>

Победитель: **[«Пахом Пихай» (Хельсинки)](https://rating.chgk.info/teams/42483)**
- Константин Изъюров
- Ольга Деркач
- Алексей Гилёв
- Владислав Быков

Второе место заняла команда [«Эмси-Эмси»](https://rating.chgk.info/teams/129) (Хельсинки), третье — [«Один и Пустота»](https://rating.chgk.info/teams/58400) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11374).


*[К оглавлению](#contents)*

---

**XVI чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 11 мая 2019 года в Хельсинки. <a name="chgk_2019"></a>

Победитель: **[«Пахом Пихай» (Хельсинки)](https://rating.chgk.info/teams/42483)**
- Эдуард Шагал
- Ксения Шагал
- Константин Изъюров
- Ольга Деркач
- Владислав Быков

Второе место заняла команда [«Мы-6»](https://rating.chgk.info/teams/3950) (Хельсинки), третье — [«Дети капитана Врунгеля»](https://rating.chgk.info/teams/133) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5524).


*[К оглавлению](#contents)*

---

**XV чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 5 мая 2018 года в Хельсинки. <a name="chgk_2018"></a>

Победитель: **[«Пахом Пихай» (Хельсинки)](https://rating.chgk.info/teams/42483)**
- Варвара Шумова
- Эдуард Шагал
- Ксения Шагал
- Константин Изъюров
- Ольга Деркач
- Владислав Быков

Второе место заняла команда [«Мы-6»](https://rating.chgk.info/teams/3950) (Хельсинки). Третье место разделили команды [«Эмси-Эмси»](https://rating.chgk.info/teams/129) (Хельсинки) и [«Кира Корпи»](https://rating.chgk.info/teams/41538) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4887).


*[К оглавлению](#contents)*

---

**XIV чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 13 мая 2017 года в Хельсинки. <a name="chgk_2017"></a>

Победитель: **[«Пахом Пихай» (Хельсинки)](https://rating.chgk.info/teams/42483)**
- Эдуард Шагал
- Ксения Шагал
- Константин Изъюров
- Ольга Деркач
- Владислав Быков

Второе место разделили команды [«Эмси-Эмси»](https://rating.chgk.info/teams/129) (Хельсинки) и [«Мы-6»](https://rating.chgk.info/teams/3950) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4299).


*[К оглавлению](#contents)*

---

**XIII чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 7 мая 2016 года в Хельсинки. <a name="chgk_2016"></a>

Победитель: **[«Пахом Пихай» (Хельсинки)](https://rating.chgk.info/teams/42483)**
- Эдуард Шагал
- Ксения Шагал
- Константин Изъюров
- Ольга Деркач
- Владислав Быков

Второе место заняла команда [«Мы-6»](https://rating.chgk.info/teams/3950) (Хельсинки), третье — [«Эмси-Эмси»](https://rating.chgk.info/teams/129) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3812).


*[К оглавлению](#contents)*

---

**XII чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 9 мая 2015 года в Хельсинки. <a name="chgk_2015"></a>

Победитель: **[«Пахом Пихай» (Хельсинки)](https://rating.chgk.info/teams/42483)**
- Эдуард Шагал
- Ксения Шагал
- Константин Изъюров
- Ольга Деркач
- Владислав Быков

Второе место заняла команда [«Дети капитана Врунгеля»](https://rating.chgk.info/teams/133) (Хельсинки), третье — [«Primus inter pares»](https://rating.chgk.info/teams/3522) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3349).


*[К оглавлению](#contents)*

---

**XI чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 9 мая 2014 года в Хельсинки. <a name="chgk_2014"></a>

Победитель: **[«Пахом Пихай» (Хельсинки)](https://rating.chgk.info/teams/42483)**
- Эдуард Шагал
- Ксения Шагал
- Константин Изъюров
- Ольга Деркач
- Владислав Быков

Второе место заняла команда [«Дети капитана Врунгеля»](https://rating.chgk.info/teams/133) (Хельсинки), третье — [«Primus inter pares»](https://rating.chgk.info/teams/3522) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2890).


*[К оглавлению](#contents)*

---

**X чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 31 мая 2013 года в Хельсинки. <a name="chgk_2013"></a>

Победитель: **[«Пахом Пихай» (Хельсинки)](https://rating.chgk.info/teams/42483)**
- Варвара Шумова
- Эдуард Шагал
- Ксения Шагал
- Константин Изъюров
- Ольга Деркач
- Владислав Быков

Второе место заняла команда [«Дети капитана Врунгеля»](https://rating.chgk.info/teams/133) (Хельсинки), третье — [«777»](https://rating.chgk.info/teams/3521) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2405).


*[К оглавлению](#contents)*

---

**IX чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 11 мая 2012 года в Хельсинки. <a name="chgk_2012"></a>

Победитель: **[«Седьмой этаж» (Хельсинки)](https://rating.chgk.info/teams/132)**
- Леван Твалтвадзе
- Руслан Суси
- Наталья Макаренко
- Виктор Древицкий
- Ольга Деркач
- Евгений Гимер
- Владислав Быков

Второе место заняла команда [«Дети капитана Врунгеля»](https://rating.chgk.info/teams/133) (Хельсинки), третье — [«777»](https://rating.chgk.info/teams/3521) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2110).


*[К оглавлению](#contents)*

---

**VIII чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 13 мая 2011 года в Хельсинки. <a name="chgk_2011"></a>

Победитель: **[«777» (Хельсинки)](https://rating.chgk.info/teams/3521)**
- Светлана Хяннинен
- Лилия Тоссавайнен
- Александр Каневский
- Алексей Выскубов
- Анастасия Власова
- Иван Власов

Второе место заняла команда [«Мы-6»](https://rating.chgk.info/teams/3950) (Хельсинки), третье — [«Седьмой этаж»](https://rating.chgk.info/teams/132) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1829).


*[К оглавлению](#contents)*

---

**VII чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 14 мая 2010 года в Хельсинки. <a name="chgk_2010"></a>

Победитель: **[«Столичные лобстеры» (Эспоо)](https://rating.chgk.info/teams/130)**
- Тимофей Целых
- Мария Пенттинен
- Алёна Вялья
- Артур Пенттинен
- Алексей Адамов

Второе место разделили команды [«Седьмой этаж»](https://rating.chgk.info/teams/132) (Хельсинки) и [«Primus inter pares»](https://rating.chgk.info/teams/3522) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/635).


*[К оглавлению](#contents)*

---

**VI чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 24 апреля 2009 года в Хельсинки. <a name="chgk_2009"></a>

Победитель: **[«777» (Хельсинки)](https://rating.chgk.info/teams/3521)**
- Светлана Хяннинен
- Лилия Тоссавайнен
- Александр Каневский
- Алексей Выскубов
- Анастасия Власова
- Иван Власов

Второе место разделили команды [«Седьмой этаж»](https://rating.chgk.info/teams/132) (Хельсинки) и [«Мы-6»](https://rating.chgk.info/teams/3950) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/451).


*[К оглавлению](#contents)*

---

**V чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 8–9 мая 2008 года в Хельсинки. <a name="chgk_2008"></a>

Победитель: **[«Мы-6» (Хельсинки)](https://rating.chgk.info/teams/3950)**
- Вадим Чупасов
- Александр Сорокин
- Алексей Сидоров
- Александр Кротов
- Екатерина Катаева
- Владимир Ищенко
- Александр Борисов

Второе место разделили команды [«777»](https://rating.chgk.info/teams/3521) (Хельсинки) и [«Primus inter pares»](https://rating.chgk.info/teams/3522) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/337).


*[К оглавлению](#contents)*

---

**IV чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 20 апреля 2007 года в Хельсинки. <a name="chgk_2007"></a>

Победитель: **[«Мы-6» (Хельсинки)](https://rating.chgk.info/teams/3950)**
- Вадим Чупасов
- Алексей Сидоров
- Александр Кротов
- Екатерина Катаева
- Владимир Ищенко
- Александр Борисов

Второе место заняла команда [«777»](https://rating.chgk.info/teams/3521) (Хельсинки). Третье место разделили команды [«Столичные лобстеры»](https://rating.chgk.info/teams/130) (Эспоо) и [«Дети капитана Врунгеля»](https://rating.chgk.info/teams/133) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/238).


*[К оглавлению](#contents)*

---

**III чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 21 апреля 2006 года в Хельсинки. <a name="chgk_2006"></a>

Победитель: **[«Мы-6» (Хельсинки)](https://rating.chgk.info/teams/3950)**

*Состав команды [«Мы-6»](https://rating.chgk.info/teams/3950) (Хельсинки) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место разделили команды [«Склочные пузырьки»](https://rating.chgk.info/teams/131) (Хельсинки), [«Дети капитана Врунгеля»](https://rating.chgk.info/teams/133) (Хельсинки) и [«777»](https://rating.chgk.info/teams/3521) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/193).


*[К оглавлению](#contents)*

---

**II чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 22 апреля 2005 года в Хельсинки. <a name="chgk_2005"></a>

Победитель: **[«Седьмой этаж» (Хельсинки)](https://rating.chgk.info/teams/132)**

*Состав команды [«Седьмой этаж»](https://rating.chgk.info/teams/132) (Хельсинки) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место разделили команды [«Столичные лобстеры»](https://rating.chgk.info/teams/130) (Эспоо) и [«Дети капитана Врунгеля»](https://rating.chgk.info/teams/133) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/94).


*[К оглавлению](#contents)*

---

**I чемпионат Финляндии по спортивному «Что? Где? Когда?»** прошёл 17 апреля 2004 года в Хельсинки. <a name="chgk_2004"></a>

Победитель: **[«Эмси-Эмси» (Хельсинки)](https://rating.chgk.info/teams/129)**

*Состав команды [«Эмси-Эмси»](https://rating.chgk.info/teams/129) (Хельсинки) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Столичные лобстеры»](https://rating.chgk.info/teams/130) (Эспоо), третье — [«Склочные пузырьки»](https://rating.chgk.info/teams/131) (Хельсинки).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/24).


*[К оглавлению](#contents)*

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
<tr><td>2025</td><td><a href="https://rating.chgk.info/tournament/12186">XIX чемпионат Финляндии по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2017</td><td><a href="https://rating.chgk.info/tournament/4299">XIV чемпионат Финляндии по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2010</td><td><a href="https://rating.chgk.info/tournament/635">VII чемпионат Финляндии по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2009</td><td><a href="https://rating.chgk.info/tournament/451">VI чемпионат Финляндии по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2008</td><td><a href="https://rating.chgk.info/tournament/337">V чемпионат Финляндии по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2006</td><td><a href="https://rating.chgk.info/tournament/193">III чемпионат Финляндии по ЧГК</a></td><td>неизвестны составы победителя и обладателей третьего места.</td></tr>
<tr><td>2005</td><td><a href="https://rating.chgk.info/tournament/94">II чемпионат Финляндии по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2004</td><td><a href="https://rating.chgk.info/tournament/24">I чемпионат Финляндии по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
