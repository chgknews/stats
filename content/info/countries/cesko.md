---
title: Чехия
weight: 1
bookToC: false
---

# Чехия

Чемпионаты Чехии проводятся с 2017 года.

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
<td><a href="https://rating.chgk.info/teams/4130">Как-то так</a></td>
<td>Прага</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/65268">В гостях у Кафки</a></td>
<td>Прага</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/54152">Пражские горцы</a></td>
<td>Прага</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/28476">Ярость Вассермана</a></td>
<td>Прага</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/61753">Номады</a></td>
<td>Прага</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/43515">Анахорет</a></td>
<td>Прага</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/71805">Сборная Неймера</a></td>
<td>Прага</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/38682">Ведуны</a></td>
<td>Прага</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/58755">Дубль В.</a></td>
<td>Прага</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/90393">Свидетели Антидепрессантов</a></td>
<td>Прага</td>
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
<td><a href="https://rating.chgk.info/player/10910">Алексей Жилинский</a></td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36246">Антон Ширяев</a></td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21006">Павел Миронов</a></td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23487">Илья Онскуль</a></td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6520">Татьяна Галицкая</a></td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/46490">Кирилл Рукавицын</a></td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/130795">Александр Шелёмин</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/117140">Денис Руденко</a></td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23885">Елена Павлова</a></td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37390">Андрей Ярмола</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/140119">Алексей Рахманов</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10418">Михаил Ерасов</a></td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5034">Инесса Василевская</a></td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/222311">Людмила Тимонина</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9989">Марина Духнич</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/138163">Айгуль Сембаева</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22435">Евгений Неймер</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/45414">Ольга Александрова</a></td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4418">Антон Буланников</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/69141">Борис Силаков</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29939">Екатерина Соколова</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/151984">Яна Безродная</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13694">Александр Касаткин</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8550">Антон Гусаков</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/82128">Арсений Ламеко</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/158668">Вера Разумов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/142087">Виктор Свистунов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/157657">Виктория Инденбаум</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/160789">Галина Головская</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3083">Дмитрий Белявский</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/154357">Евгения Катасонова</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/176788">Екатерина Кац</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/158158">Михаил Катасонов</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27246">Наталия Руберте</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/150953">Феликс Инденбаум</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/198166">Аркадий Рушкевич</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/129988">Артур Янбеков</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/475">Джамиля Азизова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26989">Дмитрий Родионов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/97006">Елена Рубцова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20982">Мария Мироненко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19428">Николай Максимов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/101528">Полина Галуева</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32415">Регина Тухбатуллина</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/77511">Светлана Донова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8610">Фаик Гусейнов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/72242">Юлия Шевелёва</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/134173">Абдул Алиев</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/40366">Александр Лапко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/60280">Алексей Редченко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/288279">Анастасия Елантьева</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/244031">Анна Шиврина</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14795">Антон Ковтун</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/60279">Валерия Волкова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/38014">Владимир Воробьёв</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/72239">Владимир Колосов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/115162">Владимир Хлевной</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/148710">Владислав Чижиков</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/116382">Григорий Золотарёв</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/73646">Дмитрий Бочаров</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/288664">Елизавета Кийко</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/38979">Иван Портнягин</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11013">Ирина Жукова</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/60281">Маргарита Соболь</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34270">Павел Худяков</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/60278">Сергей Волков</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33540">Юлия Фукельман</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/24801">Яна Петрушкевич</a></td>
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

- [VII чемпионат Чехии по спортивному ЧГК (2025)](#chgk_2025)
- [VI чемпионат Чехии по спортивному ЧГК (2024)](#chgk_2024)
- [V чемпионат Чехии по спортивному ЧГК (2023)](#chgk_2023)
- [IV чемпионат Чехии по спортивному ЧГК (2022)](#chgk_2022)
- [III чемпионат Чехии по спортивному ЧГК (2019)](#chgk_2019)
- [II чемпионат Чехии по спортивному ЧГК (2018)](#chgk_2018)
- [I чемпионат Чехии по спортивному ЧГК (2017)](#chgk_2017)


**VII чемпионат Чехии по спортивному «Что? Где? Когда?»** прошёл 4–5 октября 2025 года в Праге. <a name="chgk_2025"></a>

Победитель: **[«В гостях у Кафки» (Прага)](https://rating.chgk.info/teams/65268)**
- Вера Разумов
- Александр Шелёмин
- Денис Руденко
- Арсений Ламеко
- Андрей Ярмола
- Илья Онскуль
- Алексей Жилинский

Второе место заняла команда [«Как-то так»](https://rating.chgk.info/teams/4130) (Прага), третье — [«Пражские горцы»](https://rating.chgk.info/teams/54152) (Прага).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12543).


*[К оглавлению](#contents)*

---

**VI чемпионат Чехии по спортивному «Что? Где? Когда?»** прошёл 12–13 октября 2024 года в Праге. <a name="chgk_2024"></a>

Победитель: **[«В гостях у Кафки» (Прага)](https://rating.chgk.info/teams/65268)**
- Айгуль Сембаева
- Александр Шелёмин
- Денис Руденко
- Андрей Ярмола
- Илья Онскуль
- Алексей Жилинский

Второе место заняла команда [«Как-то так»](https://rating.chgk.info/teams/4130) (Прага), третье — [«Пражские горцы»](https://rating.chgk.info/teams/54152) (Прага).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11296).


*[К оглавлению](#contents)*

---

**V чемпионат Чехии по спортивному «Что? Где? Когда?»** прошёл 14–15 октября 2023 года в Праге. <a name="chgk_2023"></a>

Победитель: **[«В гостях у Кафки» (Прага)](https://rating.chgk.info/teams/65268)**
- Айгуль Сембаева
- Александр Шелёмин
- Денис Руденко
- Андрей Ярмола
- Илья Онскуль
- Алексей Жилинский

Второе место заняла команда [«Как-то так»](https://rating.chgk.info/teams/4130) (Прага), третье — [«Свидетели Антидепрессантов»](https://rating.chgk.info/teams/90393) (Прага).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/9685).


*[К оглавлению](#contents)*

---

**IV чемпионат Чехии по спортивному «Что? Где? Когда?»** прошёл 29–30 октября 2022 года в Праге. <a name="chgk_2022"></a>

Победитель: **[«В гостях у Кафки» (Прага)](https://rating.chgk.info/teams/65268)**
- Александр Шелёмин
- Денис Руденко
- Андрей Ярмола
- Илья Онскуль
- Алексей Жилинский
- Дмитрий Белявский

Второе место заняла команда [«Как-то так»](https://rating.chgk.info/teams/4130) (Прага), третье — [«Пражские горцы»](https://rating.chgk.info/teams/54152) (Прага).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/6636).


*[К оглавлению](#contents)*

---

**III чемпионат Чехии по спортивному «Что? Где? Когда?»** прошёл 5–6 октября 2019 года в Праге. <a name="chgk_2019"></a>

Победитель: **[«Как-то так» (Прага)](https://rating.chgk.info/teams/4130)**
- Александр Шелёмин
- Денис Руденко
- Антон Ширяев
- Илья Онскуль
- Павел Миронов
- Алексей Жилинский
- Татьяна Галицкая

Второе место заняла команда [«Сборная Неймера»](https://rating.chgk.info/teams/71805) (Прага), третье — [«Ярость Вассермана»](https://rating.chgk.info/teams/28476) (Прага).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5825).


*[К оглавлению](#contents)*

---

**II чемпионат Чехии по спортивному «Что? Где? Когда?»** прошёл 13–14 октября 2018 года в Праге. <a name="chgk_2018"></a>

Первое место разделили команды [«Как-то так»](https://rating.chgk.info/teams/4130) (Прага) и [«Номады»](https://rating.chgk.info/teams/61753) (Прага). Состав команды [«Как-то так»](https://rating.chgk.info/teams/4130):
- Екатерина Кац
- Антон Ширяев
- Елена Павлова
- Илья Онскуль
- Павел Миронов
- Алексей Жилинский
- Татьяна Галицкая

Состав команды [«Номады»](https://rating.chgk.info/teams/61753):
- Галина Головская
- Михаил Катасонов
- Виктория Инденбаум
- Евгения Катасонова
- Феликс Инденбаум
- Виктор Свистунов
- Наталия Руберте
- Антон Гусаков

Третье место заняла команда [«Ярость Вассермана»](https://rating.chgk.info/teams/28476) (Прага).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5066).


*[К оглавлению](#contents)*

---

**I чемпионат Чехии по спортивному «Что? Где? Когда?»** прошёл 3 июня 2017 года в Праге. <a name="chgk_2017"></a>

Победитель: **[«Как-то так» (Прага)](https://rating.chgk.info/teams/4130)**
- Антон Ширяев
- Елена Павлова
- Евгений Неймер
- Павел Миронов
- Александр Касаткин
- Алексей Жилинский

Второе место заняла команда [«Анахорет»](https://rating.chgk.info/teams/43515) (Прага). Третье место разделили команды [«Ведуны»](https://rating.chgk.info/teams/38682) (Прага) и [«Дубль В.»](https://rating.chgk.info/teams/58755) (Прага).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4358).


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
<tr><td>2018</td><td><a href="https://rating.chgk.info/tournament/5066">II чемпионат Чехии по ЧГК</a></td><td>неизвестен состав обладателей второго места.</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
