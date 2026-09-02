---
title: Израиль
weight: 1
bookToC: false
---

# Израиль

Чемпионаты Израиля проводятся с 1995 года. Ниже можно увидеть статистику по всем призёрам — как командам, так и игрокам. Также в отдельной вкладке можно найти информацию обо всех чемпионатах страны. Сейчас не хватает информации о самом первом чемпионате, а также некоторых иных. Если вы что-то знаете о призёрах или их составах, напишите, пожалуйста, на почту <chgknews.info@gmail.com>.

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-chgk" aria-selected="false">Чемпионаты</button><button type="button" role="tab" data-tab="missing-data" aria-selected="false">Проблемы</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th>Команда</th><th>Город</th><th>I</th><th>II</th><th>III</th><th>∑</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/641">Братья</a></td>
<td>Тель-Авив</td>
<td>13</td>
<td>6</td>
<td>1</td>
<td>20</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/194">Десятый вал</a></td>
<td>Хайфа</td>
<td>6</td>
<td>5</td>
<td>3</td>
<td>14</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/599">Know How (StartUp)</a></td>
<td>Хайфа</td>
<td>2</td>
<td>1</td>
<td>4</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/228">Незнайка</a></td>
<td>Хайфа</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/50386">Fight Club</a></td>
<td>Тель-Авив</td>
<td>0</td>
<td>3</td>
<td>3</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/4075">Эволюция</a></td>
<td>Тель-Авив</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1014">Шалуны (Ла Гвардия)</a></td>
<td>Тель-Авив</td>
<td>0</td>
<td>1</td>
<td>4</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1642">Инфи. Ёжики</a></td>
<td>Рамат-Ган</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/89252">Отсюда и выражение</a></td>
<td>Тель-Авив</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/4869">Птица-говорун</a></td>
<td>Тель-Авив</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/226">HiQ</a></td>
<td>Хайфа</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/35931">Cmon Сова</a></td>
<td>Иерусалим</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/72865">Бристольская шкала</a></td>
<td>Хайфа</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/642">Кипарис</a></td>
<td>Ришон Ле-Цион</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/91853">Неглинка</a></td>
<td>сборная</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1215">Паутина</a></td>
<td>Иерусалим</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3602">42</a></td>
<td>Рамат-Ган</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/99146">Мория</a></td>
<td>Иерусалим</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/43452">Питер Пингвинз (Клеver)</a></td>
<td>Тель-Авив</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/5898">Тангородрим</a></td>
<td>Иерусалим</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/5258">Технион</a></td>
<td>Хайфа</td>
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
<td><a href="https://rating.chgk.info/player/31190">Илья Тальянский</a></td>
<td>13</td>
<td>5</td>
<td>0</td>
<td>18</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33456">Михаил Фрадис</a></td>
<td>13</td>
<td>5</td>
<td>0</td>
<td>18</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4226">Сусанна Бровер</a></td>
<td>12</td>
<td>2</td>
<td>3</td>
<td>17</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12747">Валентин Исраэлит</a></td>
<td>11</td>
<td>4</td>
<td>0</td>
<td>15</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18160">Олег Лейбман</a></td>
<td>6</td>
<td>4</td>
<td>1</td>
<td>11</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15152">Игорь Колмаков</a></td>
<td>4</td>
<td>4</td>
<td>3</td>
<td>11</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31898">Александр Толесников</a></td>
<td>8</td>
<td>2</td>
<td>0</td>
<td>10</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32765">Полина Усыскин</a></td>
<td>8</td>
<td>1</td>
<td>0</td>
<td>9</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31315">Владислав Тартаковский</a></td>
<td>6</td>
<td>1</td>
<td>1</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23975">Алик Палатник</a></td>
<td>2</td>
<td>3</td>
<td>3</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32583">Игорь Улановский</a></td>
<td>1</td>
<td>4</td>
<td>3</td>
<td>8</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/38003">Александр Левитас</a></td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25284">Яков Подольный</a></td>
<td>2</td>
<td>4</td>
<td>1</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27853">Владимир Садов</a></td>
<td>2</td>
<td>2</td>
<td>3</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1001">Сергей Амлинский</a></td>
<td>2</td>
<td>2</td>
<td>3</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5609">Владимир Винокур</a></td>
<td>0</td>
<td>3</td>
<td>4</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/41208">Эдуард Мительман</a></td>
<td>0</td>
<td>3</td>
<td>4</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/39454">Элинор Айсман</a></td>
<td>0</td>
<td>3</td>
<td>4</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18141">Олег Леденёв</a></td>
<td>3</td>
<td>3</td>
<td>0</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9725">Наталия Дрель</a></td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26671">Илья Ратнер</a></td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20492">Леонид Медников</a></td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22473">Елена Немец</a></td>
<td>0</td>
<td>3</td>
<td>3</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6059">Юлия Воробьева</a></td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32758">Юлия Устюжанина</a></td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37259">Юрий Яковлев</a></td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17670">Александр Лави</a></td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28970">Вадим Сигалов</a></td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/250">Илья Авербух</a></td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14342">Михаил Клейман</a></td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/84789">Алексей Шестаковский</a></td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25450">Вячеслав Полонский</a></td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17624">Галина Кушнарёва</a></td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4856">Олег Вайнштейн</a></td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/39658">Станислав Малышев</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23178">Елизавета Овдеенко</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/24162">Леонид Папков</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15964">Дарья Костенко</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30278">Лев Спивак</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15870">Серж Корский</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3677">Анна Бограчёва</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13573">Борис Карнаух</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18059">Евгений Левин</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35550">Александр Шапиро</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26298">Дмитрий Пундик</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33307">Евгений Финкель</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1438">Евгений Аренгауз</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22474">Илья Немец</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33455">Дмитрий Фрадис</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22900">Вячеслав Новгородов</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18334">Даниил Либерзон</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/39307">Илья Либерзон</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/376">Ольга Агаханова</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19190">Аркадий Мазин</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1948">Вадим Бабин</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9865">Виталий Дубровнер</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36434">Геннадий Шмидов</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21630">Ева Морозовская</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33935">Ирина Хейфец</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22251">Карен Налбандян</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/90415">Ксения Тарнавская</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3239">Марк Берлин</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23679">Софья Осминкина</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6041">Станислав Воробьёв</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2548">Тимур Барский</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21632">Роман Морозовский</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11411">Анна Зарембо</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10646">Вадим Ефимов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7173">Галина Глускер</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36529">Григорий Шпитальник</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5528">Павел Вигдорчик</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30635">Сергей Стрекавин</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/48837">Алексей Ковалевский</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21859">Алексей Мурашковский</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/172823">Алексей Файнбурд</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31355">Антон Тахтаров</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20814">Денис Микшис</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4063">Дмитрий Борок</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/81015">Дмитрий Койфман</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29521">Дмитрий Слоущ</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17342">Евгений Куприянов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36450">Евгения Шмулевич</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/95258">Илья Дубинский</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/166930">Илья Фрейдкин</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34909">Ирина Чернуха</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36452">Лев Шмулевич</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21233">Леонид Михлин</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21858">Мария Мурашковская</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18513">Мила Литовская</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18514">Михаил Литовский</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3327">Светлана Борок</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9260">Светлана Куприянова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7148">Станислав Глинский</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9342">Юлия Дидбаридзе</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/307288">Александр Пастернак</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9081">Алексей Демченко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36942">Бенни Эпштейн</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27254">Борис Рубинштейн</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29500">Виктория Слинявчук</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7803">Владимир Городецкий</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28513">Владимир Севриновский</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6822">Грей Гейстрих</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/77245">Григорий Бронштейн</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19854">Даниил Маргулис</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19814">Евгений Манусов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14894">Игорь Козакевич</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21982">Константин Мухин</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26531">Константин Радченко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/77979">Лена Ремизова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17330">Любовь Купершляк</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/77244">Людмила Башканская</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/77796">Михаил Кипнис</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14474">Михаил Клиот</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33348">Михаил Фишман</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/162605">Сергей Грехов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1940">Тамара Зеликсон</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33308">Юлия Финкель</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15031">Юрий Козьмин</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25991">Ян Приворотский</a></td>
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

- [XXVIII чемпионат Израиля по спортивному ЧГК (2026)](#chgk_2026)
- [XXVII чемпионат Израиля по спортивному ЧГК (2025)](#chgk_2025)
- [XXVI чемпионат Израиля по спортивному ЧГК (2024)](#chgk_2024)
- [XXV чемпионат Израиля по спортивному ЧГК (2023)](#chgk_2023)
- [XXIV чемпионат Израиля по спортивному ЧГК (2019)](#chgk_2019)
- [XXIII чемпионат Израиля по спортивному ЧГК (2018)](#chgk_2018)
- [XXII чемпионат Израиля по спортивному ЧГК (2017)](#chgk_2017)
- [XXI чемпионат Израиля по спортивному ЧГК (2016)](#chgk_2016)
- [XX чемпионат Израиля по спортивному ЧГК (2015)](#chgk_2015)
- [XIX чемпионат Израиля по спортивному ЧГК (2014)](#chgk_2014)
- [XVIII чемпионат Израиля по спортивному ЧГК (2013)](#chgk_2013)
- [XVII чемпионат Израиля по спортивному ЧГК (2012)](#chgk_2012)
- [XVI чемпионат Израиля по спортивному ЧГК (2011)](#chgk_2011)
- [XV чемпионат Израиля по спортивному ЧГК (2010)](#chgk_2010)
- [XIV чемпионат Израиля по спортивному ЧГК (2009)](#chgk_2009)
- [XIII чемпионат Израиля по спортивному ЧГК (2008)](#chgk_2008)
- [XII чемпионат Израиля по спортивному ЧГК (2007)](#chgk_2007)
- [XI чемпионат Израиля по спортивному ЧГК (2006)](#chgk_2006)
- [X чемпионат Израиля по спортивному ЧГК (2005)](#chgk_2005)
- [IX чемпионат Израиля по спортивному ЧГК (2004)](#chgk_2004)
- [VIII чемпионат Израиля по спортивному ЧГК (2003)](#chgk_2003)
- [VII чемпионат Израиля по спортивному ЧГК (2002)](#chgk_2002)
- [VI чемпионат Израиля по спортивному ЧГК (2001)](#chgk_2001)
- [V чемпионат Израиля по спортивному ЧГК (2000)](#chgk_2000)
- [IV чемпионат Израиля по спортивному ЧГК (1999)](#chgk_1999)
- [III чемпионат Израиля по спортивному ЧГК (1998)](#chgk_1998)
- [II чемпионат Израиля по спортивному ЧГК (1997)](#chgk_1997)
- [I чемпионат Израиля по спортивному ЧГК (1995)](#chgk_1995)


**XXVIII чемпионат Израиля по спортивному «Что? Где? Когда?»** пройдёт 10 октября 2026 года в Тель-Авиве. <a id="chgk_2026"></a>

Больше информации о турнире — [в анонсе](https://www.facebook.com/groups/309438939151833/posts/27450496921286001).

*[К оглавлению](#contents)*

---

**XXVII чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 25 октября 2025 года в Тель-Авиве. <a id="chgk_2025"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Владислав Тартаковский
- Илья Тальянский
- Владимир Садов
- Сусанна Бровер
- Сергей Амлинский

Второе место заняла команда [«Бристольская шкала»](https://rating.chgk.info/teams/72865) (Хайфа), третье — [«Отсюда и выражение»](https://rating.chgk.info/teams/89252) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12214).

*[К оглавлению](#contents)*

---

**XXVI чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 18 мая 2024 года в Тель-Авиве. <a id="chgk_2024"></a>

Победитель: **[«Отсюда и выражение» (Тель-Авив)](https://rating.chgk.info/teams/89252)**
- Илья Либерзон
- Елизавета Овдеенко
- Вячеслав Новгородов
- Даниил Либерзон
- Ольга Агаханова

Второе место заняла команда [«Братья»](https://rating.chgk.info/teams/641) (Тель-Авив), третье — [«Питер Пингвинз»](https://rating.chgk.info/teams/43452) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/10477).

*[К оглавлению](#contents)*

---

**XXV чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 13 мая 2023 года в Тель-Авиве. <a id="chgk_2023"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Владислав Тартаковский
- Илья Тальянский
- Владимир Садов
- Сусанна Бровер
- Сергей Амлинский

Второе место заняла команда [«Неглинка»](https://rating.chgk.info/teams/91853) (сборная), третье — [Fight Club](https://rating.chgk.info/teams/50386) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/6353).

*[К оглавлению](#contents)*

---

**XXIV чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 1 июня 2019 года в Тель-Авиве. <a id="chgk_2019"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Полина Усыскин
- Александр Толесников
- Владислав Тартаковский
- Илья Тальянский
- Валентин Исраэлит
- Сусанна Бровер

Второе место разделили команды [«Эволюция»](https://rating.chgk.info/teams/4075) (Тель-Авив) и [Fight Club](https://rating.chgk.info/teams/50386) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5674).

*[К оглавлению](#contents)*

---

**XXIII чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 5 мая 2018 года в Тель-Авиве. <a id="chgk_2018"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Полина Усыскин
- Александр Толесников
- Владислав Тартаковский
- Илья Тальянский
- Валентин Исраэлит
- Сусанна Бровер

Второе место заняла команда [«Эволюция»](https://rating.chgk.info/teams/4075) (Тель-Авив), третье — [Fight Club](https://rating.chgk.info/teams/50386) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4849).

*[К оглавлению](#contents)*

---

**XXII чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 3 июня 2017 года в Тель-Авиве. <a id="chgk_2017"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Полина Усыскин
- Александр Толесников
- Илья Тальянский
- Валентин Исраэлит
- Сусанна Бровер

Второе место заняла команда [«Инфи. Ёжики»](https://rating.chgk.info/teams/1642) (Рамат-Ган). Третье место разделили команды [«Эволюция»](https://rating.chgk.info/teams/4075) (Тель-Авив) и [Fight Club](https://rating.chgk.info/teams/50386) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4348).

*[К оглавлению](#contents)*

---

**XXI чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 9 апреля 2016 года в Тель-Авиве. <a id="chgk_2016"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Полина Усыскин
- Александр Толесников
- Владислав Тартаковский
- Илья Тальянский
- Валентин Исраэлит
- Сусанна Бровер

Второе место заняла команда [Fight Club](https://rating.chgk.info/teams/50386) (Тель-Авив), третье — [«Ла Гвардия»](https://rating.chgk.info/teams/1014) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3767).

*[К оглавлению](#contents)*

---

**XX чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 28 марта 2015 года в Тель-Авиве. <a id="chgk_2015"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Полина Усыскин
- Александр Толесников
- Владислав Тартаковский
- Илья Тальянский
- Валентин Исраэлит
- Сусанна Бровер

Второе место заняла команда [Fight Club](https://rating.chgk.info/teams/50386) (Тель-Авив). Третье место разделили команды [«Инфи. Ёжики»](https://rating.chgk.info/teams/1642) (Рамат-Ган) и [«Птица-говорун»](https://rating.chgk.info/teams/4869) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3175).

*[К оглавлению](#contents)*

---

**XIX чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 21 марта 2014 года в Тель-Авиве. <a id="chgk_2014"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Полина Усыскин
- Александр Толесников
- Илья Тальянский
- Олег Лейбман
- Валентин Исраэлит
- Сусанна Бровер

Второе место заняла команда [«Птица-говорун»](https://rating.chgk.info/teams/4869) (Тель-Авив). Третье место разделили команды [«42»](https://rating.chgk.info/teams/3602) (Рамат-Ган) и [«Тангородрим»](https://rating.chgk.info/teams/5898) (Иерусалим).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2794).

*[К оглавлению](#contents)*

---

**XVIII чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 19 апреля 2013 года в Тель-Авиве. <a id="chgk_2013"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Полина Усыскин
- Александр Толесников
- Илья Тальянский
- Олег Лейбман
- Валентин Исраэлит
- Сусанна Бровер

Второе место заняла команда [«Ла Гвардия»](https://rating.chgk.info/teams/1014) (Тель-Авив), третье — [«Инфи. Ёжики»](https://rating.chgk.info/teams/1642) (Рамат-Ган).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2364).

*[К оглавлению](#contents)*

---

**XVII чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 4 мая 2012 года в Тель-Авиве. <a id="chgk_2012"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Полина Усыскин
- Александр Толесников
- Илья Тальянский
- Олег Лейбман
- Валентин Исраэлит

Второе место заняла команда [«Эволюция»](https://rating.chgk.info/teams/4075) (Тель-Авив), третье — [«Инфи. Ёжики»](https://rating.chgk.info/teams/1642) (Рамат-Ган).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2053).

*[К оглавлению](#contents)*

---

**XVI чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 29 апреля 2011 года в Тель-Авиве. <a id="chgk_2011"></a>

Победитель: **[«Десятый вал» (Хайфа)](https://rating.chgk.info/teams/194)**
- Александр Левитас
- Илья Ратнер
- Вячеслав Полонский
- Галина Кушнарёва
- Вадим Ефимов
- Наталия Дрель
- Сусанна Бровер

Второе место заняла команда [«Братья»](https://rating.chgk.info/teams/641) (Тель-Авив), третье — [«Ла Гвардия»](https://rating.chgk.info/teams/1014) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1796).

*[К оглавлению](#contents)*

---

**XV чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 23 апреля 2010 года в Тель-Авиве. <a id="chgk_2010"></a>

Победитель: **[«Десятый вал» (Хайфа)](https://rating.chgk.info/teams/194)**
- Илья Ратнер
- Вячеслав Полонский
- Леонид Медников
- Галина Кушнарёва
- Наталия Дрель
- Сусанна Бровер

Второе место заняла команда [«Братья»](https://rating.chgk.info/teams/641) (Тель-Авив), третье — [StartUp](https://rating.chgk.info/teams/599) (Хайфа).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/630).

*[К оглавлению](#contents)*

---

**XIV чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 1–2 мая 2009 года в Тель-Авиве. <a id="chgk_2009"></a>

Победитель: **[«Эволюция» (Тель-Авив)](https://rating.chgk.info/teams/4075)**
- Юлия Устюжанина
- Игорь Улановский
- Сергей Стрекавин
- Алик Палатник
- Игорь Колмаков
- Галина Глускер
- Павел Вигдорчик

Второе место заняла команда [«Братья»](https://rating.chgk.info/teams/641) (Тель-Авив), третье — [«Десятый вал»](https://rating.chgk.info/teams/194) (Хайфа).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/471).

*[К оглавлению](#contents)*

---

**XIII чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 1–2 мая 2008 года в Тель-Авиве. <a id="chgk_2008"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Александр Левитас
- Михаил Фрадис
- Илья Тальянский
- Яков Подольный
- Олег Лейбман
- Валентин Исраэлит

Второе место заняла команда [«Кипарис»](https://rating.chgk.info/teams/642) (Ришон Ле-Цион), третье — [«Десятый вал»](https://rating.chgk.info/teams/194) (Хайфа).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/335).

*[К оглавлению](#contents)*

---

**XII чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 6 мая 2007 года в Тель-Авиве. <a id="chgk_2007"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Илья Тальянский
- Леонид Папков
- Олег Лейбман
- Игорь Колмаков
- Валентин Исраэлит

Второе место заняла команда [StartUp](https://rating.chgk.info/teams/599) (Хайфа), третье — [«Десятый вал»](https://rating.chgk.info/teams/194) (Хайфа).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/245).

*[К оглавлению](#contents)*

---

**XI чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 5 мая 2006 года в Тель-Авиве. <a id="chgk_2006"></a>

Победитель: **[«Десятый вал» (Хайфа)](https://rating.chgk.info/teams/194)**
- Станислав Малышев
- Александр Левитас
- Яков Подольный
- Леонид Медников
- Олег Леденёв
- Наталия Дрель
- Сусанна Бровер

Второе место заняла команда [«Братья»](https://rating.chgk.info/teams/641) (Тель-Авив), третье — [Know How](https://rating.chgk.info/teams/599) (Хайфа).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/163).

*[К оглавлению](#contents)*

---

**X чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 20 мая 2005 года в Тель-Авиве. <a id="chgk_2005"></a>

Победитель: **[«Братья» (Тель-Авив)](https://rating.chgk.info/teams/641)**
- Михаил Фрадис
- Дмитрий Фрадис
- Илья Тальянский
- Олег Лейбман
- Игорь Колмаков
- Валентин Исраэлит

Второе место заняла команда [«Десятый вал»](https://rating.chgk.info/teams/194) (Хайфа), третье — [Know How](https://rating.chgk.info/teams/599) (Хайфа).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/102).

*[К оглавлению](#contents)*

---

**IX чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 7 мая 2004 года в Тель-Авиве. <a id="chgk_2004"></a>

Победитель: **[«Десятый вал» (Хайфа)](https://rating.chgk.info/teams/194)**

*Состав команды [«Десятый вал»](https://rating.chgk.info/teams/194) (Хайфа) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Братья»](https://rating.chgk.info/teams/641) (Тель-Авив), третье — [«Ла Гвардия»](https://rating.chgk.info/teams/1014) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/21).

*[К оглавлению](#contents)*

---

**VIII чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 2 мая 2003 года в Тель-Авиве. <a id="chgk_2003"></a>

Победитель: **[«Незнайка» (Хайфа)](https://rating.chgk.info/teams/228)**

*Состав команды [«Незнайка»](https://rating.chgk.info/teams/228) (Хайфа) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Десятый вал»](https://rating.chgk.info/teams/194) (Хайфа), третье — [«Шалуны»](https://rating.chgk.info/teams/1014) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1381).

*[К оглавлению](#contents)*

---

**VII чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 3 мая 2002 года в Тель-Авиве. <a id="chgk_2002"></a>

Победитель: **[«Незнайка» (Хайфа)](https://rating.chgk.info/teams/228)**
- Алексей Шестаковский
- Григорий Шпитальник
- Илья Немец
- Юлия Воробьева
- Олег Вайнштейн
- Евгений Аренгауз

Второе место заняла команда [«Десятый вал»](https://rating.chgk.info/teams/194) (Хайфа), третье — [«Братья»](https://rating.chgk.info/teams/641) (Тель-Авив).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1270).

*[К оглавлению](#contents)*

---

**VI чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 18 мая 2001 года в Хайфе. <a id="chgk_2001"></a>

Победитель: **[«Незнайка» (Хайфа)](https://rating.chgk.info/teams/228)**
- Алексей Шестаковский
- Илья Немец
- Игорь Колмаков
- Юлия Воробьева
- Олег Вайнштейн
- Евгений Аренгауз

Второе место заняла команда [«Десятый вал»](https://rating.chgk.info/teams/194) (Хайфа), третье — [Know How](https://rating.chgk.info/teams/599) (Хайфа).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1150).

*[К оглавлению](#contents)*

---

**V чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 12 мая 2000 года в Хайфе. <a id="chgk_2000"></a>

Победитель: **[«Десятый вал» (Хайфа)](https://rating.chgk.info/teams/194)**
- Олег Леденёв

Второе место заняла команда [Cmon Сова](https://rating.chgk.info/teams/35931) (Иерусалим), третье — [«Незнайка»](https://rating.chgk.info/teams/228) (Хайфа).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1056).

*[К оглавлению](#contents)*

---

**IV чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 7 мая 1999 года в Хайфе. <a id="chgk_1999"></a>

Победитель: **[HiQ (Хайфа)](https://rating.chgk.info/teams/226)**
- Анна Зарембо

Второе место заняла команда [«Десятый вал»](https://rating.chgk.info/teams/194) (Хайфа), третье — [«Технион»](https://rating.chgk.info/teams/5258) (Хайфа).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1166).

*[К оглавлению](#contents)*

---

**III чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 18 апреля 1998 года в Тель-Авиве. <a id="chgk_1998"></a>

Победитель: **[«Десятый вал» (Хайфа)](https://rating.chgk.info/teams/194)**
- Олег Леденёв

Второе место заняла команда [«Паутина»](https://rating.chgk.info/teams/1215) (Иерусалим), третье — [«Незнайка»](https://rating.chgk.info/teams/228) (Хайфа).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/716).

*[К оглавлению](#contents)*

---

**II чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл 12 апреля 1997 года в Хайфе. <a id="chgk_1997"></a>

Победитель: **[Know How (Хайфа)](https://rating.chgk.info/teams/599)**
- Алик Палатник

Второе место заняла команда [«Незнайка»](https://rating.chgk.info/teams/228) (Хайфа), третье — [«Мория»](https://rating.chgk.info/teams/99146) (Иерусалим).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/10870).

*[К оглавлению](#contents)*

---

**I чемпионат Израиля по спортивному «Что? Где? Когда?»** прошёл в 1995 году. Город проведения пока неизвестен. <a id="chgk_1995"></a>

Победитель: **[Know How (Хайфа)](https://rating.chgk.info/teams/599)**

*Состав команды [Know How](https://rating.chgk.info/teams/599) (Хайфа) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*


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
<tr><td>2024</td><td><a href="https://rating.chgk.info/tournament/10477">XXVI чемпионат Израиля по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2019</td><td><a href="https://rating.chgk.info/tournament/5674">XXIV чемпионат Израиля по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2018</td><td><a href="https://rating.chgk.info/tournament/4849">XXIII чемпионат Израиля по ЧГК</a></td><td>неизвестен состав обладателей второго места.</td></tr>
<tr><td>2004</td><td><a href="https://rating.chgk.info/tournament/21">IX чемпионат Израиля по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2003</td><td><a href="https://rating.chgk.info/tournament/1381">VIII чемпионат Израиля по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2002</td><td><a href="https://rating.chgk.info/tournament/1270">VII чемпионат Израиля по ЧГК</a></td><td>неизвестны составы обладателей второго и третьего мест.</td></tr>
<tr><td>1995</td><td>I чемпионат Израиля по ЧГК</td><td>неизвестны составы победителя и обладателей второго и третьего мест, место проведения турнира, точная дата проведения турнира.</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
