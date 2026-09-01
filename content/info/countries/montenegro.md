---
title: Черногория
weight: 1
bookToC: false
---

# Черногория

Чемпионаты Черногории проводятся с 2025 года.

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-chgk" aria-selected="false">Чемпионаты</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th>Команда</th><th>Город</th><th>I</th><th>II</th><th>III</th><th>∑</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/104474">Боромир сыграл бы лучше</a></td>
<td>сборная</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/95858">Плавалагуна</a></td>
<td>Подгорица</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/105778">Сбежанинка</a></td>
<td>Будва</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/95661">Орден Тропических Пингвинов</a></td>
<td>Подгорица</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/91493">План Б</a></td>
<td>Будва</td>
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
<td><a href="https://rating.chgk.info/player/198089">Георгий Струков</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31983">Мария Топаж</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/295133">Андрей Приходько</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/73893">Артём Сапожников</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/78358">Владислав Тарасов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/169839">Дмитрий Панкратов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/63473">Кирилл Ильин</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/16837">Наталья Кудряшова</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/339215">Роман Родионов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/56907">Татьяна Спицына</a></td>
<td>1</td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31980">Александр Топаж</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31981">Анна Топаж</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/337036">Кира Чиканцева</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/289928">Мирон Провоторов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8915">Михаил Дворкин</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/228296">Никита Ластовка</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/241293">Павел Кононенко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/246303">Тимофей Нейман</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/110808">Алекс Полисски</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4292">Александр Буберман</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/59953">Андрей Брызгалов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/301868">Анна Перова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/83954">Валерия Саварина</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/252738">Денис Лаврентьев</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/290678">Ксения Ремизонова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3253">Лина Берова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/268870">Маргарита Филатова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/342694">Мария Еременко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/290681">Ольга Буберман</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/270209">Сергей Малиновский</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-chgk"></div>

<a id="game-chgk"></a>

- [II чемпионат Черногории по спортивному ЧГК (2026)](#chgk_2026)
- [I чемпионат Черногории по спортивному ЧГК (2025)](#chgk_2025)


**II чемпионат Черногории по спортивному «Что? Где? Когда?»** прошёл 27–28 июня 2026 года в Будве. <a name="chgk_2026"></a>

Победитель: **[«Боромир сыграл бы лучше» (сборная)](https://rating.chgk.info/teams/104474)**
- Роман Родионов
- Георгий Струков
- Дмитрий Панкратов
- Кирилл Ильин
- Татьяна Спицына
- Мария Топаж

Второе место заняла команда [«Сбежанинка»](https://rating.chgk.info/teams/105778) (Будва), третье — [«План Б»](https://rating.chgk.info/teams/91493) (Будва).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12876).

---

**I чемпионат Черногории по спортивному «Что? Где? Когда?»** прошёл 29 марта 2025 года в Будве. <a name="chgk_2025"></a>

Победитель: **[«Плавалагуна» (Подгорица)](https://rating.chgk.info/teams/95858)**
- Андрей Приходько
- Владислав Тарасов
- Артём Сапожников
- Наталья Кудряшова
- Юрий Выменец

Второе место заняла команда [«Боромир сыграл бы лучше»](https://rating.chgk.info/teams/104474) (сборная), третье — [«Орден Тропических Пингвинов»](https://rating.chgk.info/teams/95661) (Подгорица).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12038).

---

<div class="country-tab-end"></div>
<div class="country-always-visible">

</div>
