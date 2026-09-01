---
title: Швейцария
weight: 1
bookToC: false
---

# Швейцария

Чемпионаты Швейцарии проводятся с 2017 года. Ниже можно увидеть статистику по всем призёрам — как командам, так и игрокам. Также в отдельной вкладке можно найти информацию обо всех чемпионатах страны.

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
<td><a href="https://rating.chgk.info/teams/53052">Эрликон</a></td>
<td>Цюрих</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/59920">Клуб 512</a></td>
<td>Берн</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/54827">Одинокий рейнджер</a></td>
<td>Женева</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/93212">Я - Сергей</a></td>
<td>Цюрих</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/79286">В поисках мема</a></td>
<td>Цюрих</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/46809">Сборная Ирландии</a></td>
<td>Дублин</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/58816">Матадор</a></td>
<td>Женева</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/59753">Постпостмодернизм</a></td>
<td>Цюрих</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/54829">Джазовый нестандарт</a></td>
<td>Женева</td>
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
<td><a href="https://rating.chgk.info/player/9535">Анна Долгая</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13682">Дмитрий Карягин</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/75645">Екатерина Наливко</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23956">Ирина Пак</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17177">Лина Кулакова</a></td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20005">Андрей Мартынов</a></td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25165">Илья Побелов</a></td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/122426">Валентина Лебедева</a></td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/117733">Александра Шенкер</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/56736">Арсений Савин</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/111958">Сергей Гришин</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/117425">Алексей Косарский</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/132035">Олег Богачук</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/132033">Юлия Зарецкая</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/124207">Алексей Можаров</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32919">Булат Фаттахов</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/171960">Лили Бауэр</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/111959">Марина Клыкова</a></td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26513">Александр Радионов</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/117426">Антон Кулинич</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/62314">Любовь Беляева</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/183106">Марина Булах</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/132034">Михаил Лебедев</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/130041">Павел Пономарёв</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/154056">Татьяна Киняпина</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14419">Алексей Климов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/199536">Алексей Могилевский</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/310572">Виолетта Кулакова</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/97731">Давид Парулава</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/138858">Денис Вшивков</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26274">Елена Пугачёва</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/225967">Иван Ульянов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/199535">Людмила Фокина</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/69720">Максим Галкин</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29447">Ярослав Скударнов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11064">Анваржон Жураев</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/144360">Андрей Афанасьев</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/200858">Анна Баташева</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/148961">Валерий Ушаков</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25552">Вероника Полянская</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/192886">Владимир Васильев</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7056">Дмитрий Гиренко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34058">Елена Холманских</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/161876">Тимур Мезенцев</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/148969">Юлия Гришина</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26686">Азамат Рахимов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/76452">Александр Косенков</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/128172">Анастасия Николье</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/148916">Анна Керечашвили</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/133599">Владимир Мартынов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/164955">Дмитрий Доброхотов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/127565">Елена Лебакина</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/270707">Мария Стефова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/270708">Петр Павленко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/132044">Пётр Гришин</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/278612">Святослав Борисов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37383">Татьяна Ярецкая</a></td>
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

- [VII чемпионат Швейцарии по спортивному ЧГК (2026)](#chgk_2026)
- [VI чемпионат Швейцарии по спортивному ЧГК (2025)](#chgk_2025)
- [V чемпионат Швейцарии по спортивному ЧГК (2024)](#chgk_2024)
- [IV чемпионат Швейцарии по спортивному ЧГК (2020)](#chgk_2020)
- [III чемпионат Швейцарии по спортивному ЧГК (2019)](#chgk_2019)
- [II чемпионат Швейцарии по спортивному ЧГК (2018)](#chgk_2018)
- [I чемпионат Швейцарии по спортивному ЧГК (2017)](#chgk_2017)


**VII чемпионат Швейцарии по спортивному «Что? Где? Когда?»** пройдёт 19–20 сентября 2026 года в Цюрихе. <a name="chgk_2026"></a>

Больше информации о турнире — [в анонсе](https://telegram.me/chgknews/1459) и [в этом телеграм-канале](https://t.me/helvetiacup).

---

**VI чемпионат Швейцарии по спортивному «Что? Где? Когда?»** прошёл 18–19 октября 2025 года в Цюрихе. <a name="chgk_2025"></a>

Победитель: **[«Сборная Ирландии» (Дублин)](https://rating.chgk.info/teams/46809)**
- Виолетта Кулакова
- Денис Вшивков
- Давид Парулава
- Ярослав Скударнов
- Елена Пугачёва
- Алексей Климов

Второе место заняла команда [«Эрликон»](https://rating.chgk.info/teams/53052) (Цюрих), третье — [«Я - Сергей»](https://rating.chgk.info/teams/93212) (Цюрих).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11987).

---

**V чемпионат Швейцарии по спортивному «Что? Где? Когда?»** прошёл 5–6 октября 2024 года в Цюрихе. <a name="chgk_2024"></a>

Победитель: **[«Эрликон» (Цюрих)](https://rating.chgk.info/teams/53052)**
- Екатерина Наливко
- Арсений Савин
- Ирина Пак
- Лина Кулакова
- Дмитрий Карягин
- Анна Долгая

Второе место заняла команда [«Клуб 512»](https://rating.chgk.info/teams/59920) (Берн), третье — [«Я - Сергей»](https://rating.chgk.info/teams/93212) (Цюрих).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11212).

---

**IV чемпионат Швейцарии по спортивному «Что? Где? Когда?»** прошёл 12 сентября 2020 года в Монтрё. <a name="chgk_2020"></a>

Победитель: **[«В поисках мема» (Цюрих)](https://rating.chgk.info/teams/79286)**
- Иван Ульянов
- Алексей Могилевский
- Людмила Фокина
- Максим Галкин
- Булат Фаттахов

Второе место заняла команда [«Постпостмодернизм»](https://rating.chgk.info/teams/59753) (Цюрих), третье — [«Одинокий рейнджер»](https://rating.chgk.info/teams/54827) (Женева).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/6705).

---

**III чемпионат Швейцарии по спортивному «Что? Где? Когда?»** прошёл 15 июня 2019 года в Лозанне. <a name="chgk_2019"></a>

Победитель: **[«Клуб 512» (Берн)](https://rating.chgk.info/teams/59920)**
- Лили Бауэр
- Александра Шенкер
- Сергей Гришин
- Булат Фаттахов
- Илья Побелов
- Андрей Мартынов

Второе место заняла команда [«Эрликон»](https://rating.chgk.info/teams/53052) (Цюрих), третье — [«Одинокий рейнджер»](https://rating.chgk.info/teams/54827) (Женева).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5723).

---

**II чемпионат Швейцарии по спортивному «Что? Где? Когда?»** прошёл 24 июня 2018 года в Лозанне. <a name="chgk_2018"></a>

Победитель: **[«Эрликон» (Цюрих)](https://rating.chgk.info/teams/53052)**
- Алексей Можаров
- Екатерина Наливко
- Ирина Пак
- Лина Кулакова
- Дмитрий Карягин
- Анна Долгая

Второе место заняла команда [«Клуб 512»](https://rating.chgk.info/teams/59920) (Берн), третье — [«Джазовый нестандарт»](https://rating.chgk.info/teams/54829) (Женева).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5051).

---

**I чемпионат Швейцарии по спортивному «Что? Где? Когда?»** прошёл 10 июня 2017 года в Женеве. <a name="chgk_2017"></a>

Победитель: **[«Эрликон» (Цюрих)](https://rating.chgk.info/teams/53052)**
- Алексей Можаров
- Екатерина Наливко
- Ирина Пак
- Лина Кулакова
- Дмитрий Карягин
- Анна Долгая

Второе место заняла команда [«Матадор»](https://rating.chgk.info/teams/58816) (Женева), третье — [«Одинокий рейнджер»](https://rating.chgk.info/teams/54827) (Женева).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4381).

---

<div class="country-tab-end"></div>
<div class="country-always-visible">

</div>
