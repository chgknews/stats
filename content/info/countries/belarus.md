---
title: Беларусь
weight: 1
bookToC: false
---

# Беларусь

Чемпионаты Беларуси проводятся с 1994 года. Более подробную информацию об истории чемпионатов Беларуси по разным интеллектуальным играм можно найти в [этой таблице](https://docs.google.com/spreadsheets/d/1fBfvMcLEkjd4wtYIIf8aHWflbJ8IOjFyqyq86OW2hjg/edit#gid=51159091). Ниже пока приведена только статистика по ЧГК.

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-chgk" aria-selected="false">Чемпионаты</button><button type="button" role="tab" data-tab="sources" aria-selected="false">Источники и благодарности</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th>Команда</th><th>Город</th><th>I</th><th>II</th><th>III</th><th>∑</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/1681">Джокер</a></td>
<td>Могилёв</td>
<td>6</td>
<td>6</td>
<td>3</td>
<td>15</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1961">Хунта</a></td>
<td>Минск</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>10</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/6936">Хронически разумные United</a></td>
<td>Минск</td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/27129">Страпелька</a></td>
<td>Минск</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/88">Хатнi Бусел (Команда Виталия Низовца)</a></td>
<td>Гомель</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1183">Умник</a></td>
<td>Минск</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/51739">Зоопарк</a></td>
<td>Минск</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1703">МИД-2</a></td>
<td>Минск</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/7864">Одушевлённые аэросани</a></td>
<td>Минск</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/718">Middle</a></td>
<td>Минск</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/66">Ультиматум</a></td>
<td>Гомель</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/29289">Зловещие сухари</a></td>
<td>Гомель</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1686">Гранд-провинция</a></td>
<td>Витебск</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/191">МаФи</a></td>
<td>Минск</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/40043">Summa Technologiae</a></td>
<td>Минск</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1165">АМО (АМО-Натюрлих)</a></td>
<td>Минск</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>Команда Камышкало</td>
<td>Брест</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/44993">Перелётный кабак</a></td>
<td>Москва</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/88369">Работяги</a></td>
<td>Витебск</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/29290">Асгард</a></td>
<td>Гомель</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1459">Белая рысь</a></td>
<td>Гомель</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/84263">Бэмби бум</a></td>
<td>сборная</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/10229">Зелёный змий</a></td>
<td>Гомель</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/83800">КЛОУНИЗМ</a></td>
<td>Минск</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1313">ЛСД-Славяне</a></td>
<td>Могилёв</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1186">Витебский трамвай</a></td>
<td>Витебск</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1148">МиФ</a></td>
<td>Минск</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/71263">Чмоки</a></td>
<td>Минск</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/4989">Штандарт</a></td>
<td>Витебск</td>
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
<td><a href="https://rating.chgk.info/player/27822">Михаил Савченков</a></td>
<td>6</td>
<td>7</td>
<td>3</td>
<td>16</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7304">Дмитрий Голдов</a></td>
<td>6</td>
<td>6</td>
<td>3</td>
<td>15</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32558">Николай Ужов</a></td>
<td>6</td>
<td>6</td>
<td>3</td>
<td>15</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26900">Руслан Ридлевич</a></td>
<td>5</td>
<td>6</td>
<td>3</td>
<td>14</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32004">Иван Топчий</a></td>
<td>4</td>
<td>5</td>
<td>4</td>
<td>13</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9785">Владислав Дронов</a></td>
<td>4</td>
<td>6</td>
<td>2</td>
<td>12</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21026">Евгений Миротин</a></td>
<td>6</td>
<td>3</td>
<td>2</td>
<td>11</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11097">Александр Забиран</a></td>
<td>4</td>
<td>4</td>
<td>3</td>
<td>11</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15964">Дарья Костенко</a></td>
<td>4</td>
<td>4</td>
<td>2</td>
<td>10</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36305">Сергей Шишко</a></td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>10</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23681">Вячеслав Осмоловский</a></td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>9</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5943">Анатолий Володченко</a></td>
<td>3</td>
<td>4</td>
<td>1</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18194">Мария Кленницкая</a></td>
<td>3</td>
<td>3</td>
<td>2</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7551">Алексей Гончаров</a></td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19510">Павел Малецкий</a></td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/100501">Никита Шевела</a></td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21560">Александр Морозов</a></td>
<td>1</td>
<td>3</td>
<td>3</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20298">Александр Матюхин</a></td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9857">Алексей Дуболазов</a></td>
<td>3</td>
<td>3</td>
<td>0</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/60043">Андрей Забавин</a></td>
<td>3</td>
<td>3</td>
<td>0</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30357">Дмитрий Старикович</a></td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36433">Александр Шмидов</a></td>
<td>3</td>
<td>0</td>
<td>3</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4417">Наталья Сиротко</a></td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/99">Герман Чепиков</a></td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27151">Николай Романовский</a></td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8444">Артём Гулецкий</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13385">Сергей Капустников</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/102968">Тимофей Прокопенко</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/40393">Юрий Разумов</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11260">Евгений Зайцев</a></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1681">Игорь Астахов</a></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29260">Сергей Сиротко</a></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54468">Андрей Танана</a></td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/38647">Виталий Калачёв</a></td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36711">Даниил Шункевич</a></td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18305">Евгений Лешкович</a></td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18132">Николай Лёгенький</a></td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14960">Сергей Козлов</a></td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/81696">Ренат Рустамов</a></td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2322">Анастасия Балмакова</a></td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4875">Елена Ваксман-Атрохова</a></td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13638">Михаил Карпук</a></td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25889">Елена Потенко</a></td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28419">Павел Свердлов</a></td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15157">Владимир Колмогоров</a></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7663">Павел Горбунов</a></td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/68633">Христина Чернушевич</a></td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/56748">Иван Сергиевич</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/132058">Наталья Шишова</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/174874">Олег Лисогурский</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/253917">Александр Ерофеев</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/253918">Алёна Ерофеева</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54469">Анна Якушевич</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36304">Ольга Шишко</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25284">Яков Подольный</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/41104">Александр Кухарчук</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5983">Алексей Волчок</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10808">Артемий Жданок</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11476">Виталий Захарик</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/90996">Владимир Осипчук</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36125">Елена Шибут</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/41383">Климентий Комиссаров</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2758">Сергей Башлыкевич</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9826">Сергей Дубелевич</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25373">Алексей Полевой</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7923">Евгений Грабовский</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25370">Кира Полевая</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15163">Наталья Колмогорова</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14868">Олег Кожедуб</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/24280">Сергей Пасиченко</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/40391">Александра Ермалович</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/255031">Анатолий Медведев</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/255032">Андрей Белевич</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/84821">Василий Гайдуков</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21258">Геннадий Мишин</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35861">Дарья Соловей</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28968">Олег Сивченко</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1000">Анна Виниченко</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14450">Леонид Климович</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29981">Андрей Солдатов</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/16871">Вадим Кузмич</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/125098">Ксения Воробьёва</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4491">Светлана Бунакова</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/82347">Александр Середа</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30601">Алексей Стома</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28442">Алина Свиб</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8057">Андрей Григорьев</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9994">Андрей Духовников</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/127861">Максим Корнеевец</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26980">Марина Родина</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11084">Павел Забавский</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1364">Сергей Апанович</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34044">Андрей Ходотов</a></td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37390">Андрей Ярмола</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/53126">Василий Бобков</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15085">Владимир Колбун</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13462">Дмитрий Карасёв</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36148">Дмитрий Шилко</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36537">Игорь Шпунгин</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/419">Илья Адамов</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27831">Михаил Сагалович</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21979">Алесь Мухин</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27429">Аркадий Рух</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30703">Виталий Струй</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21620">Мария Морозова</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/255034">Ольга Божик</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27200">Павел Ростовцев</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21586">Сергей Морозов</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32951">Татьяна Федина</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/255033">Александр Литусёв</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Александр Свирид</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/255157">Алексей Вавилов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Анна Абрамова</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/43301">Антон Иванов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/65503">Артём Сапрыко</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22634">Виталий Низовец</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/188399">Владислав Сушко</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6651">Вячеслав Гаранович</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5328">Дмитрий Великов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/75635">Дмитрий Тарасов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Евгений Числов</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/117552">Лилия Величко</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3922">Мирон Боргулёв</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/277477">Михаил Подручный</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12265">Наталья Иванова</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Наталья Камышкало</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Наталья Чирик</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Олег Черкас</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36120">Серафим Шибанов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10660">Сергей Ефимов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14456">Тамара Климович</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/41149">Александр Гаврилов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14628">Алексей Ковалёв</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Алексей Тяпугин</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/134307">Алексей Шевцов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/112314">Алина Данилова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/255257">Анастасия Акутина</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/277471">Анатолий Тимошенко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/69147">Андрей Рожков</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/137160">Анна Дубина-Красковская</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/131176">Антон Дюба</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7571">Антонина Гончарова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26429">Артём Пьянков</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8249">Валерий Громадцов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8959">Виталий Дединец</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28385">Виталий Сахарчук</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/134990">Галина Плахотная</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/255023">Денис Воробьёв</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17218">Дмитрий Кулик</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30259">Дмитрий Спектор</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Евгений Богданов</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10855">Елена Жесткова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/255021">Ирина Каплунова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29202">Кирилл Синкевич</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Людмила Богданова</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33458">Марат Фрайман</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1773">Надия Афанасьева</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33289">Николай Филон</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/113513">Пётр Игнатенко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Роман Якимец</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/317595">Сергей Клещенко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/16321">Сергей Крамич</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>Александр Данюк</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20078">Александр Марцинкевич</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30386">Александр Староказников</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/87281">Алексей Бабак</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22130">Алексей Надёжный</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26079">Алексей Прокофьев</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28774">Алексей Сенченко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/111748">Андрей Акимов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34031">Андрей Ходанович</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/85097">Анна Гедройц</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9868">Анна Дубровская</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/136310">Антон Карпиевич</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/153418">Антон Короткевич</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/74084">Антон Кушнеров</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/60092">Артём Агафонов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/112099">Валентин Копочель</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>Валерий Ермолаев</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5876">Виктория Волкова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/38193">Виталий Чумаков</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/117117">Владислав Пупшинович</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71537">Галина Сивченко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6961">Дмитрий Герчиков</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/175267">Дмитрий Красковский</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/66950">Елена Карасёва</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10920">Иван Жильцов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36481">Марина Шода</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20052">Мария Мартысевич</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9063">Михаил Дёмин</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/40753">Наталья Рутченко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/44703">Николай Сергиеня</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>Олег Сапегин</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3208">Ольга Берёзко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/121226">Павел Парфианович</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9143">Роман Денисюк</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/51020">Сергей Ржеутский</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37362">Сергей Янукович</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6284">Станислав Габрусевич</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25530">Фёдор Поляков</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2857">Юлия Бейнер</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19184">Юрий Мазаник</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-chgk"></div>

<a id="game-chgk"></a><a id="contents" name="contents"></a>

- [XXXI чемпионат Беларуси по спортивному ЧГК (2026)](#chgk_2026)
- [XXX чемпионат Беларуси по спортивному ЧГК (2025)](#chgk_2025)
- [XXIX чемпионат Беларуси по спортивному ЧГК (2024)](#chgk_2024)
- [XXVIII чемпионат Беларуси по спортивному ЧГК (2023)](#chgk_2023)
- [XXVII чемпионат Беларуси по спортивному ЧГК (2022)](#chgk_2022)
- [XXVI чемпионат Беларуси по спортивному ЧГК (2021)](#chgk_2021)
- [XXV чемпионат Беларуси по спортивному ЧГК (2019)](#chgk_2019)
- [XXIV чемпионат Беларуси по спортивному ЧГК (2018)](#chgk_2018)
- [XXIII чемпионат Беларуси по спортивному ЧГК (2017)](#chgk_2017)
- [XXII чемпионат Беларуси по спортивному ЧГК (2016)](#chgk_2016)
- [XXI чемпионат Беларуси по спортивному ЧГК (2015)](#chgk_2015)
- [XX чемпионат Беларуси по спортивному ЧГК (2014)](#chgk_2014)
- [XIX чемпионат Беларуси по спортивному ЧГК (2013)](#chgk_2013)
- [XVIII чемпионат Беларуси по спортивному ЧГК (2012)](#chgk_2012)
- [XVII чемпионат Беларуси по спортивному ЧГК (2011)](#chgk_2011)
- [XVI чемпионат Беларуси по спортивному ЧГК (2010)](#chgk_2010)
- [XV чемпионат Беларуси по спортивному ЧГК (2009)](#chgk_2009)
- [XIV чемпионат Беларуси по спортивному ЧГК (2008)](#chgk_2008)
- [XIII чемпионат Беларуси по спортивному ЧГК (2007)](#chgk_2007)
- [XII чемпионат Беларуси по спортивному ЧГК (2006)](#chgk_2006)
- [XI чемпионат Беларуси по спортивному ЧГК (2005)](#chgk_2005)
- [X чемпионат Беларуси по спортивному ЧГК (2004)](#chgk_2004)
- [IX чемпионат Беларуси по спортивному ЧГК (2003)](#chgk_2003)
- [VIII чемпионат Беларуси по спортивному ЧГК (2002)](#chgk_2002)
- [VII чемпионат Беларуси по спортивному ЧГК (2001)](#chgk_2001)
- [VI чемпионат Беларуси по спортивному ЧГК (2000)](#chgk_2000)
- [V чемпионат Беларуси по спортивному ЧГК (1999)](#chgk_1999)
- [IV чемпионат Беларуси по спортивному ЧГК (1998)](#chgk_1998)
- [III чемпионат Беларуси по спортивному ЧГК (1996)](#chgk_1996)
- [II чемпионат Беларуси по спортивному ЧГК (1995)](#chgk_1995)
- [I чемпионат Беларуси по спортивному ЧГК (1994)](#chgk_1994)


**XXXI чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 4–5 апреля 2026 года в Минске. Вопросы задавались на беларусском и русском языках. <a id="chgk_2026"></a>

Победитель: **[Хронически разумные United (Минск)](https://rating.chgk.info/teams/6936)**
- Никита Шевела
- Ренат Рустамов
- Иван Топчий
- Александр Морозов
- Павел Малецкий
- Алексей Гончаров
- Герман Чепиков

Второе место заняла команда [«КЛОУНИЗМ»](https://rating.chgk.info/teams/83800) (Минск), третье — [«Чмоки»](https://rating.chgk.info/teams/71263) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12433).

*[К оглавлению](#contents)*

---

**XXX чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 5–6 апреля 2025 года в Минске. Вопросы задавались на русском и беларусском языках. <a id="chgk_2025"></a>

Победитель: **[«Работяги» (Витебск)](https://rating.chgk.info/teams/88369)**
- Владислав Сушко
- Александр Середа
- Артём Сапрыко
- Антон Иванов
- Алексей Стома
- Владимир Колмогоров

Второе место заняла команда [«Зоопарк»](https://rating.chgk.info/teams/51739) (Минск), третье — [Хронически разумные United](https://rating.chgk.info/teams/6936) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11205).

*[К оглавлению](#contents)*

---

**XXIX чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 6–7 апреля 2024 года в Минске. <a id="chgk_2024"></a>

Победитель: **[«Зоопарк» (Минск)](https://rating.chgk.info/teams/51739)**
- Иван Сергиевич
- Андрей Танана
- Александр Кухарчук
- Виталий Калачёв
- Даниил Шункевич
- Евгений Лешкович

Второе место заняла команда [Хронически разумные United](https://rating.chgk.info/teams/6936) (Минск), третье — [«Одушевлённые аэросани»](https://rating.chgk.info/teams/7864) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/9853).

*[К оглавлению](#contents)*

---

**XXVIII чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 8–9 апреля 2023 года в Минске. Вопросы задавались на беларусском и русском языках. <a id="chgk_2023"></a>

Победитель: **[«Одушевлённые аэросани» (Минск)](https://rating.chgk.info/teams/7864)**
- Максим Корнеевец
- Ксения Воробьёва
- Иван Сергиевич
- Михаил Карпук
- Елена Ваксман-Атрохова
- Анастасия Балмакова

Второе место заняла команда [Хронически разумные United](https://rating.chgk.info/teams/6936) (Минск), третье — [«Зоопарк»](https://rating.chgk.info/teams/51739) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/8893).

*[К оглавлению](#contents)*

---

**XXVII чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 16–17 апреля 2022 года в Минске. <a id="chgk_2022"></a>

Победитель: **[«Зоопарк» (Минск)](https://rating.chgk.info/teams/51739)**
- Владимир Осипчук
- Анна Якушевич
- Андрей Танана
- Виталий Калачёв
- Даниил Шункевич
- Евгений Лешкович
- Вадим Кузмич

Второе место заняла команда [«Бэмби бум»](https://rating.chgk.info/teams/84263) (сборная), третье — [Хронически разумные United](https://rating.chgk.info/teams/6936) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/7931).

*[К оглавлению](#contents)*

---

**XXVI чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 10–11 апреля 2021 года в Минске. <a id="chgk_2021"></a>

Победитель: **[«Страпелька» (Минск)](https://rating.chgk.info/teams/27129)**
- Тимофей Прокопенко
- Никита Шевела
- Андрей Забавин
- Юрий Разумов
- Евгений Миротин
- Александр Матюхин
- Артём Гулецкий

Второе место заняла команда [«Зоопарк»](https://rating.chgk.info/teams/51739) (Минск), третье — [Middle](https://rating.chgk.info/teams/718) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/7076).

*[К оглавлению](#contents)*

---

**XXV чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 6–7 апреля 2019 года в Минске. <a id="chgk_2019"></a>

Победитель: **[«Страпелька» (Минск)](https://rating.chgk.info/teams/27129)**
- Тимофей Прокопенко
- Никита Шевела
- Андрей Забавин
- Юрий Разумов
- Евгений Миротин
- Александр Матюхин
- Артём Гулецкий

Второе место заняла команда [Middle](https://rating.chgk.info/teams/718) (Минск), третье — [«Одушевлённые аэросани»](https://rating.chgk.info/teams/7864) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5538).

*[К оглавлению](#contents)*

---

**XXIV чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 24–25 марта 2018 года в Минске. <a id="chgk_2018"></a>

Победитель: **[«Страпелька» (Минск)](https://rating.chgk.info/teams/27129)**
- Тимофей Прокопенко
- Андрей Забавин
- Юрий Разумов
- Евгений Миротин
- Александр Матюхин
- Артём Гулецкий

Второе место заняла команда [«Одушевлённые аэросани»](https://rating.chgk.info/teams/7864) (Минск), третье — [Хронически разумные United](https://rating.chgk.info/teams/6936) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4712).

*[К оглавлению](#contents)*

---

**XXIII чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 1–2 апреля 2017 года в Минске. <a id="chgk_2017"></a>

Победитель: **[Middle (Минск)](https://rating.chgk.info/teams/718)**
- Климентий Комиссаров
- Елена Шибут
- Виталий Захарик
- Артемий Жданок
- Сергей Дубелевич
- Сергей Апанович

Второе место заняла команда [«Страпелька»](https://rating.chgk.info/teams/27129) (Минск), третье — [«Штандарт»](https://rating.chgk.info/teams/4989) (Витебск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4228).

*[К оглавлению](#contents)*

---

**XXII чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 13–14 февраля 2016 года в Минске. <a id="chgk_2016"></a>

Победитель: **[Хронически разумные United (Минск)](https://rating.chgk.info/teams/6936)**
- Иван Топчий
- Александр Матюхин
- Павел Малецкий
- Мария Кленницкая
- Алексей Гончаров
- Алексей Волчок
- Сергей Башлыкевич

Второе место заняла команда [«Страпелька»](https://rating.chgk.info/teams/27129) (Минск), третье — [Summa Technologiae](https://rating.chgk.info/teams/40043) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3690).

*[К оглавлению](#contents)*

---

**XXI чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 14–15 февраля 2015 года в Минске. <a id="chgk_2015"></a>

Победитель: **[«Джокер» (Могилёв)](https://rating.chgk.info/teams/1681)**
- Николай Ужов
- Дмитрий Старикович
- Михаил Савченков
- Евгений Миротин
- Алексей Дуболазов
- Дмитрий Голдов

Второе место заняла команда [Хронически разумные United](https://rating.chgk.info/teams/6936) (Минск), третье — [«Одушевлённые аэросани»](https://rating.chgk.info/teams/7864) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3176).

*[К оглавлению](#contents)*

---

**XX чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 7–8 марта 2014 года в Минске. <a id="chgk_2014"></a>

Победитель: **[«Перелётный кабак» (Москва)](https://rating.chgk.info/teams/44993)**
- Серафим Шибанов
- Николай Романовский
- Дарья Костенко
- Владислав Дронов
- Вячеслав Гаранович
- Дмитрий Великов

Второе место заняла команда [«Джокер»](https://rating.chgk.info/teams/1681) (Могилёв), третье — [«МИД-2»](https://rating.chgk.info/teams/1703) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2799).

*[К оглавлению](#contents)*

---

**XIX чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 15–16 февраля 2013 года в Минске. <a id="chgk_2013"></a>

Победитель: **[«Джокер» (Могилёв)](https://rating.chgk.info/teams/1681)**
- Николай Ужов
- Андрей Солдатов
- Михаил Савченков
- Руслан Ридлевич
- Алексей Дуболазов
- Дмитрий Голдов

Второе место заняла команда [«МИД-2»](https://rating.chgk.info/teams/1703) (Минск), третье — [Summa Technologiae](https://rating.chgk.info/teams/40043) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2300).

*[К оглавлению](#contents)*

---

**XVIII чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 10–11 февраля 2012 года в Минске. <a id="chgk_2012"></a>

Победитель: **[«МИД-2» (Минск)](https://rating.chgk.info/teams/1703)**
- Дмитрий Старикович
- Павел Свердлов
- Евгений Миротин
- Мария Кленницкая
- Николай Лёгенький
- Сергей Козлов
- Сергей Ефимов

Второе место заняла команда [«Хунта»](https://rating.chgk.info/teams/1961) (Минск), третье — [«Умник»](https://rating.chgk.info/teams/1183) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2032).

*[К оглавлению](#contents)*

---

**XVII чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 11–12 февраля 2011 года в Минске. <a id="chgk_2011"></a>

Победитель: **[«Хунта» (Минск)](https://rating.chgk.info/teams/1961)**
- Александр Шмидов
- Сергей Шишко
- Иван Топчий
- Дарья Костенко
- Владислав Дронов
- Анатолий Володченко
- Светлана Бунакова

Второе место заняла команда [«Джокер»](https://rating.chgk.info/teams/1681) (Могилёв), третье — [«МИД-2»](https://rating.chgk.info/teams/1703) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1733).

*[К оглавлению](#contents)*

---

**XVI чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 12–13 февраля 2010 года в Минске. <a id="chgk_2010"></a>

Победитель: **[«МИД-2» (Минск)](https://rating.chgk.info/teams/1703)**
- Дмитрий Старикович
- Павел Свердлов
- Евгений Миротин
- Мария Кленницкая
- Николай Лёгенький
- Сергей Козлов

Второе место заняла команда [«Джокер»](https://rating.chgk.info/teams/1681) (Могилёв), третье — [«Хунта»](https://rating.chgk.info/teams/1961) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/582).

*[К оглавлению](#contents)*

---

**XV чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 13 февраля 2009 года в Витебске. <a id="chgk_2009"></a>

Победитель: **[«Джокер» (Могилёв)](https://rating.chgk.info/teams/1681)**
- Николай Ужов
- Михаил Савченков
- Руслан Ридлевич
- Александр Забиран
- Алексей Дуболазов
- Дмитрий Голдов

Второе место заняла команда [«Хунта»](https://rating.chgk.info/teams/1961) (Минск), третье — [«Ультиматум»](https://rating.chgk.info/teams/66) (Гомель).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/426).

*[К оглавлению](#contents)*

---

**XIV чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 15 февраля 2008 года в Витебске. <a id="chgk_2008"></a>

Победитель: **[«Хунта» (Минск)](https://rating.chgk.info/teams/1961)**
- Сергей Шишко
- Иван Топчий
- Дарья Костенко
- Владислав Дронов
- Анатолий Володченко
- Наталья Сиротко

Второе место заняла команда [«МаФи»](https://rating.chgk.info/teams/191) (Минск), третье — [«Джокер»](https://rating.chgk.info/teams/1681) (Могилёв).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/308).

*[К оглавлению](#contents)*

---

**XIII чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 9 марта 2007 года в Минске. <a id="chgk_2007"></a>

Победитель: **[«Джокер» (Могилёв)](https://rating.chgk.info/teams/1681)**
- Николай Ужов
- Михаил Савченков
- Руслан Ридлевич
- Вячеслав Осмоловский
- Александр Забиран
- Дмитрий Голдов

Второе место заняла команда [«Хунта»](https://rating.chgk.info/teams/1961) (Минск), третье — [«Ультиматум»](https://rating.chgk.info/teams/66) (Гомель).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/220).

*[К оглавлению](#contents)*

---

**XII чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 25–26 февраля 2006 года в Витебске. Вопросы задавались на беларусском и русском языках. <a id="chgk_2006"></a>

Победитель: **[«Ультиматум» (Гомель)](https://rating.chgk.info/teams/66)**
- Александр Шмидов
- Алексей Полевой
- Кира Полевая
- Сергей Пасиченко
- Олег Кожедуб
- Евгений Грабовский

Второе место заняла команда [«Джокер»](https://rating.chgk.info/teams/1681) (Могилёв), третье — [«Умник»](https://rating.chgk.info/teams/1183) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/8486).

*[К оглавлению](#contents)*

---

**XI чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 26 февраля 2005 года в Минске. <a id="chgk_2005"></a>

Победитель: **[«Хунта» (Минск)](https://rating.chgk.info/teams/1961)**
- Сергей Шишко
- Ольга Шишко
- Дарья Костенко
- Владислав Дронов
- Павел Горбунов
- Анатолий Володченко
- Мирон Боргулёв

Второе место заняла команда [«Джокер»](https://rating.chgk.info/teams/1681) (Могилёв), третье — [«МаФи»](https://rating.chgk.info/teams/191) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/85).

*[К оглавлению](#contents)*

---

**X чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 20 февраля 2004 года в Могилёве. <a id="chgk_2004"></a>

Победитель: **[«Умник» (Минск)](https://rating.chgk.info/teams/1183)**
- Сергей Сиротко
- Алина Свиб
- Николай Романовский
- Евгений Зайцев
- Павел Забавский
- Игорь Астахов

Второе место заняла команда [«Хунта»](https://rating.chgk.info/teams/1961) (Минск), третье — [«Джокер»](https://rating.chgk.info/teams/1681) (Могилёв).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/23).

*[К оглавлению](#contents)*

---

**IX чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 7 февраля 2003 года в Минске. <a id="chgk_2003"></a>

Победитель: **[Хатнi Бусел (Гомель)](https://rating.chgk.info/teams/88)**
- Алексей Вавилов
- Александр Шмидов
- Виталий Низовец
- Леонид Климович
- Сергей Капустников
- Наталья Иванова

Второе место заняла команда [«Хунта»](https://rating.chgk.info/teams/1961) (Минск), третье — [«МиФ»](https://rating.chgk.info/teams/1148) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1393).

*[К оглавлению](#contents)*

---

**VIII чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 9 февраля 2002 года в Минске. <a id="chgk_2002"></a>

Победитель: **[«Джокер» (Могилёв)](https://rating.chgk.info/teams/1681)**
- Николай Ужов
- Михаил Савченков
- Руслан Ридлевич
- Вячеслав Осмоловский
- Александр Забиран
- Дмитрий Голдов

Второе место заняла команда [«ЛСД-Славяне»](https://rating.chgk.info/teams/1313) (Могилёв), третье — [«Хунта»](https://rating.chgk.info/teams/1961) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1242).

*[К оглавлению](#contents)*

---

**VII чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 9 февраля 2001 года в Могилёве. <a id="chgk_2001"></a>

Победитель: **[«Гранд-провинция» (Витебск)](https://rating.chgk.info/teams/1686)**
- Александр Литусёв
- Наталья Шишова
- Наталья Колмогорова
- Владимир Колмогоров
- Андрей Духовников
- Андрей Григорьев

Второе место заняла команда [«Джокер»](https://rating.chgk.info/teams/1681) (Могилёв), третье — [«Зловещие сухари»](https://rating.chgk.info/teams/29289) (Гомель).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1088).

*[К оглавлению](#contents)*

---

**VI чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 7–8 мая 2000 года в Гомеле. <a id="chgk_2000"></a>

Победитель: **[«Умник» (Минск)](https://rating.chgk.info/teams/1183)**
- Дмитрий Тарасов
- Сергей Сиротко
- Николай Романовский
- Марина Родина
- Евгений Зайцев
- Игорь Астахов

Второе место заняла команда [Хатнi Бусел](https://rating.chgk.info/teams/88) (Гомель), третье — [«Гранд-провинция»](https://rating.chgk.info/teams/1686) (Витебск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1090).

*[К оглавлению](#contents)*

---

**V чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 7–8 мая 1999 года в Гомеле. <a id="chgk_1999"></a>

Победитель: **[Хатнi Бусел (Гомель)](https://rating.chgk.info/teams/88)**
- Алёна Ерофеева
- Александр Ерофеев
- Олег Лисогурский
- Елена Потенко
- Яков Подольный
- Сергей Капустников

Второе место заняла команда [«Асгард»](https://rating.chgk.info/teams/29290) (Гомель), третье — [«АМО»](https://rating.chgk.info/teams/1165) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1443).

*[К оглавлению](#contents)*

---

**IV чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 21–22 марта 1998 года в Могилёве. <a id="chgk_1998"></a>

Победитель: **[«Умник» (Минск)](https://rating.chgk.info/teams/1183)**
- Михаил Подручный
- Олег Лисогурский
- Сергей Сиротко
- Николай Романовский
- Евгений Зайцев
- Игорь Астахов

Второе место заняла команда [Хатнi Бусел](https://rating.chgk.info/teams/88) (Гомель), третье — [«Джокер»](https://rating.chgk.info/teams/1681) (Могилёв).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/9509).

*[К оглавлению](#contents)*

---

**III чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 19 сентября 1996 года в Минске. <a id="chgk_1996"></a>

Победитель: **[Хатнi Бусел (Гомель)](https://rating.chgk.info/teams/88)**
- Леонид Климович
- Сергей Капустников
- Елена Потенко
- Наталья Шишова
- Тамара Климович
- Олег Черкас

Второе место заняла команда [«Зловещие сухари»](https://rating.chgk.info/teams/29289) (Гомель), третье — [«Витебский трамвай»](https://rating.chgk.info/teams/1186) (Витебск).

*[К оглавлению](#contents)*

---

**II чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 6–8 мая 1995 года в Гомеле. <a id="chgk_1995"></a>

Победитель: **[«Джокер» (Могилёв)](https://rating.chgk.info/teams/1681)**
- Николай Ужов
- Михаил Савченков
- Руслан Ридлевич
- Вячеслав Осмоловский
- Александр Забиран
- Дмитрий Голдов

Второе место заняла команда [«Зелёный змий»](https://rating.chgk.info/teams/10229) (Гомель), третье — [«АМО»](https://rating.chgk.info/teams/1165) (Минск).

*[К оглавлению](#contents)*

---

**I чемпионат Беларуси по спортивному «Что? Где? Когда?»** прошёл 7–9 мая 1994 года в Гомеле. <a id="chgk_1994"></a>

Победитель: **«Команда Камышкало» (Брест)**
- Анна Абрамова
- Лилия Величко
- Наталья Камышкало
- Александр Свирид
- Наталья Чирик
- Евгений Числов

Второе место заняла команда [«Белая рысь»](https://rating.chgk.info/teams/1459) (Гомель), третье — [«Зловещие сухари»](https://rating.chgk.info/teams/29289) (Гомель).

*[К оглавлению](#contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="sources"></div>

<a id="sources"></a>

Здесь указан список источников, откуда взята та или иная информация на этой странице. Огромную работу для наполнение этой страницы проделали авторы [«Летописи чемпионатов Беларуси»](https://docs.google.com/spreadsheets/d/1fBfvMcLEkjd4wtYIIf8aHWflbJ8IOjFyqyq86OW2hjg/edit?gid=518101333#gid=518101333). Спасибо им за это!

<table>
<thead>
<tr><th>Турнир</th><th>Год</th><th>Источник</th></tr>
</thead>
<tbody>
<tr><td>III чемпионат Беларуси по ЧГК</td><td>1996</td><td><a href="https://docs.google.com/spreadsheets/d/1fBfvMcLEkjd4wtYIIf8aHWflbJ8IOjFyqyq86OW2hjg/edit?gid=51159091#gid=51159091">Летопись ЧРБ</a></td></tr>
<tr><td>II чемпионат Беларуси по ЧГК</td><td>1995</td><td><a href="https://docs.google.com/spreadsheets/d/1fBfvMcLEkjd4wtYIIf8aHWflbJ8IOjFyqyq86OW2hjg/edit?gid=51159091#gid=51159091">Летопись ЧРБ</a></td></tr>
<tr><td>I чемпионат Беларуси по ЧГК</td><td>1994</td><td><a href="https://docs.google.com/spreadsheets/d/1fBfvMcLEkjd4wtYIIf8aHWflbJ8IOjFyqyq86OW2hjg/edit?gid=51159091#gid=51159091">Летопись ЧРБ</a></td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
