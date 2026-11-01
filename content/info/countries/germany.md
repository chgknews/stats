---
title: Германия
weight: 1
bookToC: false
---

# Германия

Чемпионаты Германии проводятся с 1998 года.

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
<td><a href="https://rating.chgk.info/teams/330">Против ветра (Проти вiтру)</a></td>
<td>Дюссельдорф</td>
<td>9</td>
<td>4</td>
<td>1</td>
<td>14</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/201">Крейзер Аврора</a></td>
<td>Бохум</td>
<td>2</td>
<td>4</td>
<td>2</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/54151">Йота Киля</a></td>
<td>Дрезден</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/51253">Жмурки</a></td>
<td>Мюнхен</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/5067">Страх и ужас</a></td>
<td>Кёльн</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/2694">Оки-Доки</a></td>
<td>Мюнхен</td>
<td>1</td>
<td>5</td>
<td>4</td>
<td>10</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/276">Ералаш</a></td>
<td>Дюссельдорф</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/2377">Семь пядей</a></td>
<td>Франкфурт-на-Майне</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/72474">Шутка со смыслом</a></td>
<td>Мюнхен</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>2 капитана</td>
<td>сборная</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/29687">Мама мия</a></td>
<td>Мюнхен</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/85345">Рой Макай</a></td>
<td>сборная</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/540">Стирол</a></td>
<td>Горловка</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3166">Понты Пилата</a></td>
<td>Берлин</td>
<td>0</td>
<td>5</td>
<td>2</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/551">Филателисты им. Грибоедова</a></td>
<td>Кёльн</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/6081">Thunderbolt (Тандерболт)</a></td>
<td>Франкфурт-на-Майне</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/6790">Тёмный лес</a></td>
<td>Мюнхен</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3217">Джон и Катапульта</a></td>
<td>Дортмунд</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/97357">И 2</a></td>
<td>Дюссельдорф</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/68786">Сцилла</a></td>
<td>Берлин</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/248">Цимес</a></td>
<td>Дортмунд</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/85037">Странные агенты</a></td>
<td>Берлин</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/42296">Устами Младенца</a></td>
<td>Кёльн</td>
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
<td><a href="https://rating.chgk.info/player/17811">Александр Ланин</a></td>
<td>11</td>
<td>3</td>
<td>2</td>
<td>16</td>
<td>11</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4261">Борис Брукман</a></td>
<td>9</td>
<td>5</td>
<td>2</td>
<td>16</td>
<td>9</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/24511">Михаил Перлин</a></td>
<td>9</td>
<td>5</td>
<td>2</td>
<td>16</td>
<td>9</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29256">Павел Сироткин</a></td>
<td>10</td>
<td>3</td>
<td>1</td>
<td>14</td>
<td>10</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26989">Дмитрий Родионов</a></td>
<td>9</td>
<td>4</td>
<td>1</td>
<td>14</td>
<td>9</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20397">Александр Мачевский</a></td>
<td>3</td>
<td>4</td>
<td>4</td>
<td>11</td>
<td>3</td>
<td>4</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6545">Илья Галле</a></td>
<td>1</td>
<td>6</td>
<td>4</td>
<td>11</td>
<td>1</td>
<td>6</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27209">Виктория Рохленко</a></td>
<td>1</td>
<td>5</td>
<td>4</td>
<td>10</td>
<td>1</td>
<td>5</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8550">Антон Гусаков</a></td>
<td>1</td>
<td>6</td>
<td>2</td>
<td>9</td>
<td>1</td>
<td>6</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3251">Валерий Беров</a></td>
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
<td><a href="https://rating.chgk.info/player/14821">Дмитрий Коган</a></td>
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
<td><a href="https://rating.chgk.info/player/6525">Александр Галкин</a></td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>7</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9573">Борис Долинский</a></td>
<td>0</td>
<td>5</td>
<td>2</td>
<td>7</td>
<td>0</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18323">Максим Ли</a></td>
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
<td><a href="https://rating.chgk.info/player/4870">Александр Ваксман</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2475">Михаил Барчук</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35009">Дмитрий Чесноков</a></td>
<td>1</td>
<td>4</td>
<td>1</td>
<td>6</td>
<td>1</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1340">Виктор Анцелевич</a></td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>6</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7287">Борис Гоз</a></td>
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
<td><a href="https://rating.chgk.info/player/64436">Кирилл Берёзкин</a></td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33759">Борис Ханукаев</a></td>
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
<td><a href="https://rating.chgk.info/player/10785">Анна Ждан</a></td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>4</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30180">Роман Сорокин</a></td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>4</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21976">Михаил Мухачёв</a></td>
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
<td><a href="https://rating.chgk.info/player/72279">Денис Шабанов</a></td>
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
<td><a href="https://rating.chgk.info/player/53816">Елена Даскал</a></td>
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
<td><a href="https://rating.chgk.info/player/13287">Леонид Кандыба</a></td>
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
<td><a href="https://rating.chgk.info/player/27246">Наталия Руберте</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4856">Олег Вайнштейн</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34270">Павел Худяков</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18938">Эдуард Лурье</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1616">Юрий Аршанский</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8183">Евгений Грицевский</a></td>
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
<td><a href="https://rating.chgk.info/player/20981">Василина Мироненко</a></td>
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
<td><a href="https://rating.chgk.info/player/7896">Ирина Готлибович</a></td>
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
<td><a href="https://rating.chgk.info/player/4878">Сергей Вакуленко</a></td>
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
<td><a href="https://rating.chgk.info/player/35999">Алёна Шенгелия</a></td>
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
<td><a href="https://rating.chgk.info/player/19235">Борис Майзель</a></td>
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
<td><a href="https://rating.chgk.info/player/15810">Евгения Королинская</a></td>
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
<td><a href="https://rating.chgk.info/player/18189">Марк Ленивкер</a></td>
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
<td><a href="https://rating.chgk.info/player/18490">Дмитрий Литвинов</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35385">Эдуард Шагал</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9834">Ольга Дубинская</a></td>
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
<td><a href="https://rating.chgk.info/player/36483">Борис Шойхет</a></td>
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
<td><a href="https://rating.chgk.info/player/112486">Евгений Федько</a></td>
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
<td><a href="https://rating.chgk.info/player/12401">Егор Игнатенков</a></td>
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
<td><a href="https://rating.chgk.info/player/13740">Жаннета Кат</a></td>
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
<td><a href="https://rating.chgk.info/player/21504">Илья Моргунов</a></td>
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
<td><a href="https://rating.chgk.info/player/115772">Александр Потапенко</a></td>
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
<td><a href="https://rating.chgk.info/player/17024">Владислав Кузькоков</a></td>
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
<td><a href="https://rating.chgk.info/player/17230">Егор Куликов</a></td>
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
<td><a href="https://rating.chgk.info/player/62619">Илья Струков</a></td>
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
<td><a href="https://rating.chgk.info/player/2465">Александр Барба</a></td>
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
<td><a href="https://rating.chgk.info/player/5583">Алексей Виноградов</a></td>
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
<td><a href="https://rating.chgk.info/player/30352">Иван Стариков</a></td>
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
<td><a href="https://rating.chgk.info/player/24698">Павел Петров</a></td>
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
<td><a href="https://rating.chgk.info/player/27491">Павел Рывкин</a></td>
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
<td><a href="https://rating.chgk.info/player/5607">Юлия Виноградова</a></td>
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
<td><a href="https://rating.chgk.info/player/35998">Александр Шенгелия</a></td>
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
<td><a href="https://rating.chgk.info/player/54136">Амаль Имангулов</a></td>
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
<td><a href="https://rating.chgk.info/player/34846">Антон Чернин</a></td>
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
<td><a href="https://rating.chgk.info/player/8968">Елена Дедова</a></td>
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
<td><a href="https://rating.chgk.info/player/82128">Арсений Ламеко</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26441">Николай Пятаев</a></td>
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
<td><a href="https://rating.chgk.info/player/16829">Алина Хайтлина</a></td>
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
<td><a href="https://rating.chgk.info/player/59898">Артур Матвеев</a></td>
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
<td><a href="https://rating.chgk.info/player/16507">Елена Кригер</a></td>
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
<td><a href="https://rating.chgk.info/player/21375">Максим Мозуль</a></td>
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
<td><a href="https://rating.chgk.info/player/10293">Михаил Екимов</a></td>
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
<td><a href="https://rating.chgk.info/player/11019">Михаил Жуковский</a></td>
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
<td><a href="https://rating.chgk.info/player/19428">Николай Максимов</a></td>
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
<td><a href="https://rating.chgk.info/player/9733">Родислав Дрибен</a></td>
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
<td><a href="https://rating.chgk.info/player/36208">Роман Шипов</a></td>
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
<td><a href="https://rating.chgk.info/player/129837">Антон Моисеев</a></td>
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
<td><a href="https://rating.chgk.info/player/36592">Алексей Штых</a></td>
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
<td><a href="https://rating.chgk.info/player/5665">Анна Вишневская</a></td>
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
<td><a href="https://rating.chgk.info/player/13912">Анна Зайдель</a></td>
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
<td><a href="https://rating.chgk.info/player/7479">Анна Кандыба</a></td>
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
<td><a href="https://rating.chgk.info/player/37147">Борис Юхвец</a></td>
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
<td><a href="https://rating.chgk.info/player/15313">Евгения Комарова</a></td>
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
<td><a href="https://rating.chgk.info/player/9972">Елена Дурмашкина</a></td>
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
<td><a href="https://rating.chgk.info/player/101864">Елизавета Лысенко</a></td>
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
<td><a href="https://rating.chgk.info/player/24899">Кирилл Пиксендеев</a></td>
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
<td><a href="https://rating.chgk.info/player/16329">Ксения Шагал</a></td>
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
<td><a href="https://rating.chgk.info/player/49157">Леонид Тимофеев</a></td>
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
<td><a href="https://rating.chgk.info/player/25882">Максим Поташев</a></td>
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
<td><a href="https://rating.chgk.info/player/29032">Максим Сидоров</a></td>
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
<td><a href="https://rating.chgk.info/player/22063">Марианна Брукман</a></td>
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
<td><a href="https://rating.chgk.info/player/18194">Мария Кленницкая</a></td>
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
<td><a href="https://rating.chgk.info/player/77673">Михаил Папков</a></td>
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
<td><a href="https://rating.chgk.info/player/5643">Ольга Витес</a></td>
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
<td><a href="https://rating.chgk.info/player/134991">Павел Семенюк</a></td>
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
<td><a href="https://rating.chgk.info/player/1646">Ровшан Аскеров</a></td>
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
<td><a href="https://rating.chgk.info/player/20691">Станислав Мереминский</a></td>
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
<td><a href="https://rating.chgk.info/player/9806">Татьяна Дружинина</a></td>
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
<td><a href="https://rating.chgk.info/player/27257">Татьяна Рубинштейн</a></td>
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
<td><a href="https://rating.chgk.info/player/33651">Юрий Хайчин</a></td>
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
<td><a href="https://rating.chgk.info/player/56000">Евгений Коватенков</a></td>
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
<td><a href="https://rating.chgk.info/player/5290">Александр Ведехин</a></td>
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
<td><a href="https://rating.chgk.info/player/9383">Александр Диниц</a></td>
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
<td><a href="https://rating.chgk.info/player/14057">Александр Кимков</a></td>
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
<td><a href="https://rating.chgk.info/player/24283">Александр Пастернак</a></td>
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
<td><a href="https://rating.chgk.info/player/108288">Александр Сновский</a></td>
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
<td><a href="https://rating.chgk.info/player/26911">Александр Фингеров</a></td>
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
<td><a href="https://rating.chgk.info/player/3240">Александра Берлина</a></td>
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
<td><a href="https://rating.chgk.info/player/2746">Алина Баширова</a></td>
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
<td><a href="https://rating.chgk.info/player/4439">Алла Булашевская</a></td>
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
<td><a href="https://rating.chgk.info/player/4307">Анатолий Бугаев</a></td>
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
<td><a href="https://rating.chgk.info/player/307285">Борис Колигаев</a></td>
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
<td><a href="https://rating.chgk.info/player/29675">Виктория Смирнова</a></td>
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
<td><a href="https://rating.chgk.info/player/75320">Галина Денискина</a></td>
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
<td><a href="https://rating.chgk.info/player/9784">Глеб Дрепин</a></td>
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
<td><a href="https://rating.chgk.info/player/39334">Дмитрий Арбузов</a></td>
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
<td><a href="https://rating.chgk.info/player/3344">Дмитрий Бибичков</a></td>
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
<td><a href="https://rating.chgk.info/player/37730">Дмитрий Попов</a></td>
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
<td><a href="https://rating.chgk.info/player/37584">Иван Ерёмин</a></td>
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
<td><a href="https://rating.chgk.info/player/50840">Илана Пастернак</a></td>
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
<td><a href="https://rating.chgk.info/player/69939">Инна Калитухо</a></td>
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
<td><a href="https://rating.chgk.info/player/130709">Михаил Алимов</a></td>
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
<td><a href="https://rating.chgk.info/player/53031">Михаил Карачун</a></td>
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
<td><a href="https://rating.chgk.info/player/35823">Наталия Шебалина</a></td>
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
<td><a href="https://rating.chgk.info/player/22978">Николай Новицкий</a></td>
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
<td><a href="https://rating.chgk.info/player/129955">Ольга Флегонтова</a></td>
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
<td><a href="https://rating.chgk.info/player/2005">Пётр Бавин</a></td>
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
<td><a href="https://rating.chgk.info/player/8082">Сергей Григ</a></td>
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
<td><a href="https://rating.chgk.info/player/39906">Теймур Бабаев</a></td>
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
<td><a href="https://rating.chgk.info/player/11220">Аскар Заитов</a></td>
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
<td><a href="https://rating.chgk.info/player/138163">Айгуль Сембаева</a></td>
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
<td><a href="https://rating.chgk.info/player/76212">Александр Большун</a></td>
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
<td><a href="https://rating.chgk.info/player/133103">Александр Волков</a></td>
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
<td><a href="https://rating.chgk.info/player/200858">Анна Баташева</a></td>
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
<td><a href="https://rating.chgk.info/player/71061">Анна Свирина</a></td>
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
<td><a href="https://rating.chgk.info/player/37173">Аркадий Яблонский</a></td>
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
<td><a href="https://rating.chgk.info/player/27046">Вениамин Розенфельд</a></td>
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
<td><a href="https://rating.chgk.info/player/192886">Владимир Васильев</a></td>
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
<td><a href="https://rating.chgk.info/player/49286">Владимир Замятин</a></td>
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
<td><a href="https://rating.chgk.info/player/41360">Владимир Рупанов</a></td>
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
<td><a href="https://rating.chgk.info/player/35477">Владимир Шалгунов</a></td>
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
<td><a href="https://rating.chgk.info/player/28856">Григорий Сергиенко</a></td>
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
<td><a href="https://rating.chgk.info/player/201073">Елизавета Зиновьева</a></td>
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
<td><a href="https://rating.chgk.info/player/104732">Илона Прикуле</a></td>
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
<td><a href="https://rating.chgk.info/player/16075">Ирина Котляр</a></td>
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
<td><a href="https://rating.chgk.info/player/16076">Константин Котляр</a></td>
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
<td><a href="https://rating.chgk.info/player/307286">Лада Гутникова</a></td>
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
<td><a href="https://rating.chgk.info/player/20332">Леонид Махлин</a></td>
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
<td><a href="https://rating.chgk.info/player/23342">Леонид Окнянский</a></td>
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
<td><a href="https://rating.chgk.info/player/6523">Маргарита Чикобава</a></td>
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
<td><a href="https://rating.chgk.info/player/16077">Олег Котляр</a></td>
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
<td><a href="https://rating.chgk.info/player/8636">Сергей Гутников</a></td>
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

- [XXV чемпионат Германии по спортивному ЧГК (2025)](#chgk_2025)
- [XXIV чемпионат Германии по спортивному ЧГК (2024)](#chgk_2024)
- [XXIII чемпионат Германии по спортивному ЧГК (2023)](#chgk_2023)
- [XXII чемпионат Германии по спортивному ЧГК (2019)](#chgk_2019)
- [XXI чемпионат Германии по спортивному ЧГК (2018)](#chgk_2018)
- [XX чемпионат Германии по спортивному ЧГК (2017)](#chgk_2017)
- [XIX чемпионат Германии по спортивному ЧГК (2016)](#chgk_2016)
- [XVIII чемпионат Германии по спортивному ЧГК (2015)](#chgk_2015)
- [XVII чемпионат Германии по спортивному ЧГК (2014)](#chgk_2014)
- [XVI чемпионат Германии по спортивному ЧГК (2013)](#chgk_2013)
- [XV чемпионат Германии по спортивному ЧГК (2012)](#chgk_2012)
- [XIV чемпионат Германии по спортивному ЧГК (2011)](#chgk_2011)
- [XIII чемпионат Германии по спортивному ЧГК (2010)](#chgk_2010)
- [XII чемпионат Германии по спортивному ЧГК (2009)](#chgk_2009)
- [XI чемпионат Германии по спортивному ЧГК (2008)](#chgk_2008)
- [X чемпионат Германии по спортивному ЧГК (2007)](#chgk_2007)
- [IX чемпионат Германии по спортивному ЧГК (2006)](#chgk_2006)
- [VIII чемпионат Германии по спортивному ЧГК (2004)](#chgk_2004)
- [VII чемпионат Германии по спортивному ЧГК (2003)](#chgk_2003)
- [VI чемпионат Германии по спортивному ЧГК (2002)](#chgk_2002)
- [V чемпионат Германии по спортивному ЧГК (2001)](#chgk_2001)
- [IV чемпионат Германии по спортивному ЧГК (2000)](#chgk_2000)
- [III чемпионат Германии по спортивному ЧГК (1999)](#chgk_1999)
- [II чемпионат Германии по спортивному ЧГК (1998)](#chgk_1998)
- [I чемпионат Германии по спортивному ЧГК (1997)](#chgk_1997)


**XXV чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 8–9 ноября 2025 года в Мюнхене. <a id="chgk_2025"></a>

Победитель: **[«Шутка со смыслом» (Мюнхен)](https://rating.chgk.info/teams/72474)**
- Амаль Имангулов
- Роман Сорокин
- Мария Кленницкая
- Анна Ждан
- Татьяна Дружинина
- Елена Дедова

Второе место заняла команда [«Сцилла»](https://rating.chgk.info/teams/68786) (Берлин), третье — [«Йота Киля»](https://rating.chgk.info/teams/54151) (Дрезден).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12839). Больше информации о турнире — [в этом телеграм-канале](https://t.me/ChampWasWoWann/313) и [здесь](https://t.me/chgknews/1298).

*[К оглавлению](#chgk_contents)*

---

**XXIV чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 2–3 ноября 2024 года в Мюнхене. <a id="chgk_2024"></a>

Победитель: **[«Йота Киля» (Дрезден)](https://rating.chgk.info/teams/54151)**
- Денис Шабанов
- Кирилл Берёзкин
- Дмитрий Чесноков
- Антон Чернин
- Александр Ваксман
- Михаил Барчук

Второе место заняла команда [Проти вiтру](https://rating.chgk.info/teams/330) (Дюссельдорф). Третье место разделили команды [«Шутка со смыслом»](https://rating.chgk.info/teams/72474) (Мюнхен) и [«Странные агенты»](https://rating.chgk.info/teams/85037) (Берлин).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11022). Фотографии с турнира можно посмотреть по [этой ссылке](https://t.me/ChampWasWoWann/181). Больше информации о турнире — [в этом телеграм-канале](https://t.me/ChampWasWoWann) и [здесь](https://t.me/chgknews/975).

*[К оглавлению](#chgk_contents)*

---

**XXIII чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 4–5 ноября 2023 года в Мюнхене. <a id="chgk_2023"></a>

Победитель: **[«Рой Макай» (сборная)](https://rating.chgk.info/teams/85345)**
- Павел Семенюк
- Елизавета Лысенко
- Михаил Папков
- Алексей Штых
- Эдуард Шагал
- Ксения Шагал

Второе место заняла команда [«И 2»](https://rating.chgk.info/teams/97357) (Дюссельдорф), третье — [«Йота Киля»](https://rating.chgk.info/teams/54151) (Дрезден).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/9677). Фотографии с турнира можно посмотреть по [этой ссылке](https://t.me/ChampWasWoWann/66). Больше информации о турнире — [в этом телеграм-канале](https://t.me/ChampWasWoWann/92) и [здесь](https://t.me/chgknews/644).

*[К оглавлению](#chgk_contents)*

---

**XXII чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 11 мая 2019 года в Бад-Киссингене. <a id="chgk_2019"></a>

Победитель: **[«Йота Киля» (Дрезден)](https://rating.chgk.info/teams/54151)**
- Кирилл Берёзкин
- Елена Даскал
- Иван Стариков
- Антон Гусаков
- Александр Ваксман
- Михаил Барчук

Второе место заняла команда [«Тёмный лес»](https://rating.chgk.info/teams/6790) (Мюнхен), третье — [«Против ветра»](https://rating.chgk.info/teams/330) (Дюссельдорф).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5424).

*[К оглавлению](#chgk_contents)*

---

**XXI чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 5 мая 2018 года в Бад-Киссингене. <a id="chgk_2018"></a>

Победитель: **[«Жмурки» (Мюнхен)](https://rating.chgk.info/teams/51253)**
- Александр Потапенко
- Илья Струков
- Роман Сорокин
- Александр Мачевский
- Егор Куликов
- Владислав Кузькоков
- Анна Ждан

Второе место разделили команды [«Понты Пилата»](https://rating.chgk.info/teams/3166) (Берлин) и [«Йота Киля»](https://rating.chgk.info/teams/54151) (Дрезден).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4859).

*[К оглавлению](#chgk_contents)*

---

**XX чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 10 июня 2017 года в Бад-Киссингене. <a id="chgk_2017"></a>

Победитель: **[«Жмурки» (Мюнхен)](https://rating.chgk.info/teams/51253)**
- Александр Потапенко
- Илья Струков
- Роман Сорокин
- Александр Мачевский
- Егор Куликов
- Владислав Кузькоков
- Анна Ждан

Второе место разделили команды [«Против ветра»](https://rating.chgk.info/teams/330) (Дюссельдорф) и [«Понты Пилата»](https://rating.chgk.info/teams/3166) (Берлин).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4265).

*[К оглавлению](#chgk_contents)*

---

**XIX чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 21 мая 2016 года в Бад-Киссингене. <a id="chgk_2016"></a>

Победитель: **[«Против ветра» (Дюссельдорф)](https://rating.chgk.info/teams/330)**
- Павел Сироткин
- Дмитрий Родионов
- Михаил Перлин
- Василина Мироненко
- Александр Ланин
- Борис Брукман

Второе место заняла команда [«Джон и Катапульта»](https://rating.chgk.info/teams/3217) (Дортмунд), третье — [«Понты Пилата»](https://rating.chgk.info/teams/3166) (Берлин).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3742).

*[К оглавлению](#chgk_contents)*

---

**XVIII чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 6–7 июня 2015 года в Бад-Киссингене. <a id="chgk_2015"></a>

Победитель: **[«Против ветра» (Дюссельдорф)](https://rating.chgk.info/teams/330)**
- Павел Сироткин
- Дмитрий Родионов
- Михаил Перлин
- Василина Мироненко
- Александр Ланин
- Борис Брукман

Второе место заняла команда [«Понты Пилата»](https://rating.chgk.info/teams/3166) (Берлин), третье — [«Оки-Доки»](https://rating.chgk.info/teams/2694) (Мюнхен).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3347).

*[К оглавлению](#chgk_contents)*

---

**XVII чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 9–10 мая 2014 года в Бад-Киссингене. <a id="chgk_2014"></a>

Победитель: **[«Против ветра» (Дюссельдорф)](https://rating.chgk.info/teams/330)**
- Павел Сироткин
- Дмитрий Родионов
- Михаил Перлин
- Александр Ланин
- Борис Брукман

Второе место заняла команда [«Оки-Доки»](https://rating.chgk.info/teams/2694) (Мюнхен), третье — [«Крейзер Аврора»](https://rating.chgk.info/teams/201) (Бохум).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2885).

*[К оглавлению](#chgk_contents)*

---

**XVI чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 19 апреля 2013 года в Бад-Киссингене. <a id="chgk_2013"></a>

Победитель: **[«Против ветра» (Дюссельдорф)](https://rating.chgk.info/teams/330)**
- Павел Сироткин
- Дмитрий Родионов
- Михаил Перлин
- Александр Ланин
- Александр Галкин
- Борис Брукман

Второе место заняла команда [«Оки-Доки»](https://rating.chgk.info/teams/2694) (Мюнхен), третье — [«Тёмный лес»](https://rating.chgk.info/teams/6790) (Мюнхен).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2358).

*[К оглавлению](#chgk_contents)*

---

**XV чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 4 мая 2012 года в Бад-Киссингене. <a id="chgk_2012"></a>

Победитель: **[«Против ветра» (Дюссельдорф)](https://rating.chgk.info/teams/330)**
- Павел Сироткин
- Дмитрий Родионов
- Михаил Перлин
- Александр Ланин
- Александр Галкин
- Борис Брукман

Второе место заняла команда [«Оки-Доки»](https://rating.chgk.info/teams/2694) (Мюнхен), третье — [«Семь пядей»](https://rating.chgk.info/teams/2377) (Франкфурт-на-Майне).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2122).

*[К оглавлению](#chgk_contents)*

---

**XIV чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 29–30 апреля 2011 года в Бад-Киссингене. <a id="chgk_2011"></a>

Победитель: **[«Против ветра» (Дюссельдорф)](https://rating.chgk.info/teams/330)**
- Павел Сироткин
- Дмитрий Родионов
- Михаил Перлин
- Александр Ланин
- Александр Галкин
- Борис Брукман

Второе место разделили команды [«Оки-Доки»](https://rating.chgk.info/teams/2694) (Мюнхен) и [«Понты Пилата»](https://rating.chgk.info/teams/3166) (Берлин).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1916), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3766).

*[К оглавлению](#chgk_contents)*

---

**XIII чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 23 апреля 2010 года в Бад-Киссингене. <a id="chgk_2010"></a>

Победитель: **[«Оки-Доки» (Мюнхен)](https://rating.chgk.info/teams/2694)**
- Виктория Рохленко
- Кирилл Пиксендеев
- Павел Петров
- Александр Мачевский
- Дмитрий Коган
- Илья Галле
- Валерий Беров

Второе место заняла команда [«Против ветра»](https://rating.chgk.info/teams/330) (Дюссельдорф), третье — [«Понты Пилата»](https://rating.chgk.info/teams/3166) (Берлин).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/628), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3957).

*[К оглавлению](#chgk_contents)*

---

**XII чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 24–25 апреля 2009 года в Бад-Киссингене. <a id="chgk_2009"></a>

Победитель: **[«Против ветра» (Дюссельдорф)](https://rating.chgk.info/teams/330)**
- Павел Сироткин
- Дмитрий Родионов
- Михаил Перлин
- Александр Ланин
- Александр Галкин
- Борис Брукман

Второе место заняла команда [«Понты Пилата»](https://rating.chgk.info/teams/3166) (Берлин), третье — [«Оки-Доки»](https://rating.chgk.info/teams/2694) (Мюнхен).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/448), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4259). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20090502192431/http://www.znatoki.de/index.html).

*[К оглавлению](#chgk_contents)*

---

**XI чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 24–25 апреля 2008 года в Бад-Киссингене. <a id="chgk_2008"></a>

Победитель: **[«Против ветра» (Дюссельдорф)](https://rating.chgk.info/teams/330)**
- Павел Сироткин
- Дмитрий Родионов
- Михаил Перлин
- Александр Ланин
- Александр Галкин
- Борис Брукман

Второе место заняла команда [«Семь пядей»](https://rating.chgk.info/teams/2377) (Франкфурт-на-Майне), третье — [«Оки-Доки»](https://rating.chgk.info/teams/2694) (Мюнхен).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/354), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4822). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/200804BadKissingen.html).

*[К оглавлению](#chgk_contents)*

---

**X чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 12 мая 2007 года в Бад-Киссингене. <a id="chgk_2007"></a>

Победитель: **[«Семь пядей» (Франкфурт-на-Майне)](https://rating.chgk.info/teams/2377)**
- Борис Юхвец
- Максим Сидоров
- Павел Рывкин
- Марианна Брукман
- Марк Ленивкер
- Евгения Комарова

Второе место заняла команда [«Против ветра»](https://rating.chgk.info/teams/330) (Дюссельдорф), третье — [«Оки-Доки»](https://rating.chgk.info/teams/2694) (Мюнхен).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/248), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4597). Больше информации о турнире — [здесь](https://web.archive.org/web/20080214202200/http://www.znatoki.de/turniry/Vesna/ChGSummary.htm) и [в Летописи](http://letopis.chgk.info/200705BadKissingen.html).

*[К оглавлению](#chgk_contents)*

---

**IX чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 29 апреля 2006 года в Бад-Киссингене. <a id="chgk_2006"></a>

Победитель: **[«Против ветра» (Дюссельдорф)](https://rating.chgk.info/teams/330)**
- Павел Сироткин
- Дмитрий Родионов
- Михаил Перлин
- Александр Ланин
- Борис Брукман

Второе место разделили команды [«Ералаш»](https://rating.chgk.info/teams/276) (Дюссельдорф), [«Филателисты им. Грибоедова»](https://rating.chgk.info/teams/551) (Кёльн) и [«Оки-Доки»](https://rating.chgk.info/teams/2694) (Мюнхен).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/171), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4281). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20070915092709/http://www.znatoki.de/arhiv/turniry/chempi.html), [здесь](https://web.archive.org/web/20080214230306/http://www.znatoki.de/arhiv/turniry/2006/ChempGer/Summary.htm) и [в Летописи](http://letopis.chgk.info/200604Germany.html).

*[К оглавлению](#chgk_contents)*

---

**VIII чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 3–5 декабря 2004 года в Обербернардсе. <a id="chgk_2004"></a>

Победитель: **[«Страх и ужас» (Кёльн)](https://rating.chgk.info/teams/5067)**
- Ольга Витес
- Ирина Готлибович
- Борис Гоз
- Павел Сироткин
- Елена Дурмашкина
- Анна Зайдель
- Татьяна Рубинштейн
- Станислав Мереминский

Второе место заняла команда [«Филателисты им. Грибоедова»](https://rating.chgk.info/teams/551) (Кёльн), третье — [«Крейзер Аврора»](https://rating.chgk.info/teams/201) (Бохум). Турнир проводился на вопросах Открытого кубка России.

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournaments/62), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3808).

*[К оглавлению](#chgk_contents)*

---

**VII чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 5–7 декабря 2003 года в Вольфштайне. <a id="chgk_2003"></a>

Победитель: **[«Ералаш» (Дюссельдорф)](https://rating.chgk.info/teams/276)**
- Юлия Виноградова
- Алексей Виноградов
- Александр Барба
- Алёна Шенгелия
- Александр Шенгелия
- Михаил Мухачёв
- Анна Кандыба

Второе место заняла команда [«Крейзер Аврора»](https://rating.chgk.info/teams/201) (Бохум), третье — [«Филателисты им. Грибоедова»](https://rating.chgk.info/teams/551) (Кёльн). Турнир проводился на вопросах Открытого кубка России.

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournaments/16), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3287).

*[К оглавлению](#chgk_contents)*

---

**VI чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 30 ноября 2002 года в Эрбахе. <a id="chgk_2002"></a>

Победитель: **[«Крейзер Аврора» (Бохум)](https://rating.chgk.info/teams/201)**

*Состав команды [«Крейзер Аврора»](https://rating.chgk.info/teams/201) (Бохум) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Ералаш»](https://rating.chgk.info/teams/276) (Дюссельдорф), третье — [«Филателисты им. Грибоедова»](https://rating.chgk.info/teams/551) (Кёльн). Турнир проводился на вопросах Открытого кубка России.

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1325), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/2614).

*[К оглавлению](#chgk_contents)*

---

**V чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 30 ноября–2 декабря 2001 года в Вассеркуппе. <a id="chgk_2001"></a>

Победитель: **[«Страх и ужас» (Кёльн)](https://rating.chgk.info/teams/5067)**

*Состав команды [«Страх и ужас»](https://rating.chgk.info/teams/5067) (Кёльн) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Крейзер Аврора»](https://rating.chgk.info/teams/201) (Бохум), третье — [«Тандерболт»](https://rating.chgk.info/teams/6081) (Франкфурт-на-Майне). Турнир проводился на вопросах Открытого кубка России.

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournaments/1337), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/1985).

*[К оглавлению](#chgk_contents)*

---

**IV чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 16 декабря 2000 года в Бахарахе. <a id="chgk_2000"></a>

Победитель: **[«Крейзер Аврора» (Бохум)](https://rating.chgk.info/teams/201)**
- Борис Майзель
- Максим Ли
- Александр Ланин
- Евгения Королинская
- Леонид Кандыба
- Борис Гоз
- Сергей Вакуленко

Второе место заняла команда [«Тандерболт»](https://rating.chgk.info/teams/6081) (Франкфурт-на-Майне), третье — [«Устами Младенца»](https://rating.chgk.info/teams/42296) (Кёльн).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/10869). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/200012Bacharach.html).

*[К оглавлению](#chgk_contents)*

---

**III чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 17–19 декабря 1999 года в Гаккенбахе. <a id="chgk_1999"></a>

Победитель: **[«Мама мия» (Мюнхен)](https://rating.chgk.info/teams/29687)**
- Михаил Мухачёв
- Ирина Готлибович
- Анна Вишневская
- Сергей Вакуленко

Второе место заняла команда [«Крейзер Аврора»](https://rating.chgk.info/teams/201) (Бохум), третье — [«Ералаш»](https://rating.chgk.info/teams/276) (Дюссельдорф).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1180). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/199912Germany.html).

*[К оглавлению](#chgk_contents)*

---

**II чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 24–26 июля 1998 года в Бонне. <a id="chgk_1998"></a>

Победитель: **[«Стирол» (Горловка)](https://rating.chgk.info/teams/540)**
- Леонид Тимофеев
- Юрий Хайчин
- Максим Поташев
- Ровшан Аскеров

Второе место заняла команда [«Крейзер Аврора»](https://rating.chgk.info/teams/201) (Бохум), третье — [«Цимес»](https://rating.chgk.info/teams/248) (Дортмунд).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1597). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/199807GermanyII.html).

*[К оглавлению](#chgk_contents)*

---

**I чемпионат Германии по спортивному «Что? Где? Когда?»** прошёл 8–9 ноября 1997 года в Лаутербахе. <a id="chgk_1997"></a>

Победитель: **«2 капитана» (сборная)**
- Максим Ли
- Александр Ланин

Второе место заняла команда [Thunderbolt](https://rating.chgk.info/teams/6081) (Дармштадт), третье — [«Цимес»](https://rating.chgk.info/teams/248) (Дортмунд).

Вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/1599). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/199711Lauterbach.html).

*[К оглавлению](#chgk_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ssi"></div>

<a id="game-ssi"></a><a id="ssi_contents" name="ssi_contents"></a>

- [XXV чемпионат Германии по ССИ (2025)](#ssi_2025)
- [XXIV чемпионат Германии по ССИ (2024)](#ssi_2024)
- [XXIII чемпионат Германии по ССИ (2023)](#ssi_2023)


**XXV чемпионат Германии по спортивной «Своей игре»** прошёл 8–9 ноября 2025 года в Мюнхене. <a id="ssi_2025"></a>

Победитель: **[Арсений Ламеко](https://rating.chgk.info/player/82128)**

Второе место занял [Кирилл Берёзкин](https://rating.chgk.info/player/64436), третье — [Эдуард Шагал](https://rating.chgk.info/player/35385). В общем (негерманском) зачёте Эдуард занял четвёртое место, третье место занял Леонид Михлин.

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1bhwI81DKxM-2aSQfyMubETjUPYB2bWIhcOoJpfbE3uI/edit?gid=1021328774#gid=1021328774). Больше информации о турнире — [в этом телеграм-канале](https://t.me/ChampWasWoWann/365) и [здесь](https://t.me/chgknews/1298).

*[К оглавлению](#ssi_contents)*

---

**XXIV чемпионат Германии по спортивной «Своей игре»** прошёл 2–3 ноября 2024 года в Мюнхене. <a id="ssi_2024"></a>

Победитель: **[Дмитрий Литвинов](https://rating.chgk.info/player/18490)**

Второе место занял [Антон Моисеев](https://rating.chgk.info/player/129837), третье — [Эдуард Шагал](https://rating.chgk.info/player/35385). В общем (негерманском) зачёте Антон занял третье место ,а Эдуард — четвёртое. Второе место занял Дмитрий Панкратов.

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1hPRkLHIH9kDaNJIcgC3w6bZUqY73G2jbxqw7kelZsJ0/edit?gid=571591260#gid=571591260). Больше информации о турнире — [в этом телеграм-канале](https://t.me/ChampWasWoWann/164) и [здесь](https://t.me/chgknews/975).

*[К оглавлению](#ssi_contents)*

---

**XXIII чемпионат Германии по спортивной «Своей игре»** прошёл 4–5 ноября 2023 года в Мюнхене. <a id="ssi_2023"></a>

Победитель: **[Евгений Коватенков](https://rating.chgk.info/player/56000)**

Второе место занял [Аскар Заитов](https://rating.chgk.info/player/11220), третье — [Дмитрий Литвинов](https://rating.chgk.info/player/18490). В общем (негерманском) зачёте турнир выиграл Илья Онскуль. Евгений Коватенков, соответственно, был вторым, Аскар Заитов — третьим, а Дмитрий Литвинов — четвёртым.

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/19LhNU0-m-4J_rxuGMC0VUJ2gq7RznARfQ4dxxlcSGlM/edit#gid=1836952984). Больше информации о турнире — [в этом телеграм-канале](https://t.me/ChampWasWoWann/92) и [здесь](https://t.me/chgknews/644).

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
<tr><td>2018</td><td><a href="https://rating.chgk.info/tournament/4859">XXI чемпионат Германии по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2017</td><td><a href="https://rating.chgk.info/tournament/4265">XX чемпионат Германии по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2011</td><td><a href="https://rating.chgk.info/tournament/1916">XIV чемпионат Германии по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2006</td><td><a href="https://rating.chgk.info/tournament/171">IX чемпионат Германии по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2002</td><td><a href="https://rating.chgk.info/tournament/1325">VI чемпионат Германии по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2001</td><td><a href="https://rating.chgk.info/tournaments/1337">V чемпионат Германии по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>1999</td><td><a href="https://rating.chgk.info/tournament/1180">III чемпионат Германии по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>1998</td><td><a href="https://rating.chgk.info/tournament/1597">II чемпионат Германии по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>1997</td><td>I чемпионат Германии по ЧГК</td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
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
<tr><td>XI чемпионат Германии по ЧГК</td><td>2008</td><td><a href="https://web.archive.org/web/20090303060806/http://www.znatoki.de/arhiv/turniry/2008/ChempGer/ChGSummary.htm">сайт znatoki.de</a> (повопросные результаты ЧГК)</td></tr>
<tr><td>X чемпионат Германии по ЧГК</td><td>2007</td><td><a href="https://web.archive.org/web/20070818092419/http://www.znatoki.de/turniry/Vesna/ChGSummary.htm#tur1">сайт znatoki.de</a> (повопросные результаты ЧГК)</td></tr>
<tr><td>IX чемпионат Германии по ЧГК</td><td>2006</td><td><a href="https://web.archive.org/web/20080214230306/http://www.znatoki.de/arhiv/turniry/2006/ChempGer/Summary.htm">сайт znatoki.de</a> (повопросные результаты ЧГК)</td></tr>
<tr><td>III чемпионат Германии по ЧГК</td><td>1999</td><td><a href="https://web.archive.org/web/20040901120036/http://www.znatoki.de/turniri.html">сайт znatoki.de</a> (даты III чемпионата Германии), <a href="https://web.archive.org/web/20080214192158/http://www.znatoki.de/arhiv/turniry/1999/chempger99.html">отчёт Михаила Перлина</a></td></tr>
<tr><td>II чемпионат Германии по ЧГК</td><td>1998</td><td><a href="https://web.archive.org/web/20040901120036/http://www.znatoki.de/turniri.html">сайт znatoki.de</a> (даты II чемпионата Германии)</td></tr>
<tr><td>XXV чемпионат Германии по ССИ</td><td>1997</td><td><a href="https://web.archive.org/web/20040901120036/http://www.znatoki.de/turniri.html">сайт znatoki.de</a> (даты I чемпионата Германии)</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
