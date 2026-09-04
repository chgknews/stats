---
title: Польша
weight: 1
bookToC: false
---

# Польша

Чемпионаты Польши проводятся с 2018 года.

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
<td><a href="https://rating.chgk.info/teams/85064">Гимназия имени прочитанного регламента (Кринж без выходных / Гимназия имени Кейси Легумины / Гимназия имени контркультурщика Юрия Яковлева)</a></td>
<td>Варшава</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/77174">Polish Space Marines</a></td>
<td>Краков</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/62709">Есть желающие</a></td>
<td>Вроцлав</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/56081">Глеб Шишкин</a></td>
<td>Краков</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/58672">WarSowiak</a></td>
<td>Варшава</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/86732">4:20</a></td>
<td>Краков</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/56078">Большие люди</a></td>
<td>Краков</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/10">1067 (Яровит)</a></td>
<td>Варшава</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/55501">7:52 (Семь сорок)</a></td>
<td>Минск</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/59514">Клёк</a></td>
<td>Варшава</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/91508">Просто чилим</a></td>
<td>Вроцлав</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/86769">Самая большая лягушка</a></td>
<td>Варшава</td>
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
<td><a href="https://rating.chgk.info/player/5611">Алексей Винокуров</a></td>
<td>5</td>
<td>1</td>
<td>0</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/9105">Сергей Демяненко</a></td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29516">Дмитрий Слободянюк</a></td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/39285">Владислава Плохих</a></td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/40390">Елена Гордынец</a></td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/40393">Юрий Разумов</a></td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5876">Виктория Волкова</a></td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/158668">Вера Разумов (Монина)</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28948">Евгений Сибиряк</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28656">Валерий Семёнов</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18168">Надежда Лейчинская</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10964">Александр Жорняк</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22491">Артём Ненашев</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22494">Наталия Ненашева</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17121">Владимир Кукарских</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35861">Дарья Соловей</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71501">Мария Завьялова</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/77785">Станислав Адаскевич</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/40366">Александр Лапко</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/78753">Антон Леоник</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11522">Елена Захарова</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/856">Теймур Алиев</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23287">Александр Огнев</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4602">Александра Бурчалова</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10989">Алексей Жуков</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/16871">Вадим Кузмич</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/84704">Дарья Степаньян</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29049">Егор Сидорович</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/140910">Илья Лопатин</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28419">Павел Свердлов</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28085">Яна Ярош</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37751">Андрей Руденко</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12401">Егор Игнатенков</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28689">Инна Семёнова</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/41383">Климентий Комиссаров</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22242">Ксения Накладова</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21952">Павел Муха</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37259">Юрий Яковлев</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/150355">Александр Бивейнис</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11329">Александр Залесский</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/142414">Александр Пышко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/305950">Алексей Кудин</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/117131">Андрей Назарчук</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28302">Валерий Сатыбалдыев</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/113703">Глеб Николаев</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7496">Екатерина Коциевская</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/148408">Елена Лещинска</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29943">Ирина Соколова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/48787">Константин Гаргер</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/91952">Ксения Пушнова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/74687">Максим Мушко</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/123158">Марина Платонова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/226275">Михаил Трифонов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27006">Нина Рожановская</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/84175">Ольга Суглобова</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/102913">Пётр Гурин</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8885">Рустем Даутов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/140697">Сергей Гребенюк</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/158945">Юрий Иванов</a></td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/145556">Аким Малыщик</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/104489">Александр Бринчук</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/151598">Александр Галкин</a></td>
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
<td><a href="https://rating.chgk.info/player/36742">Александр Шустер</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54289">Анна Ермачёнок</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32814">Антон Ушкалов</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/90997">Антон Шевченя</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17938">Владислав Латынский</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/81697">Дарья Данилевич</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/55812">Денис Валянский</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/40108">Дмитрий Сарначёв</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28247">Евгений Сарвас</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/113521">Елизавета Гришкина</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/113500">Иван Мозолюк</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/145114">Константин Пронкевич</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/156113">Мария Захарнёва</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/135512">Михаил Наталевич</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/128250">Никита Кучин</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17618">Сергей Кушмар</a></td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/55808">Яна Тарасевич</a></td>
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

- [VII чемпионат Польши по спортивному ЧГК (2026)](#chgk_2026)
- [VI чемпионат Польши по спортивному ЧГК (2025)](#chgk_2025)
- [V чемпионат Польши по спортивному ЧГК (2024)](#chgk_2024)
- [IV чемпионат Польши по спортивному ЧГК (2023)](#chgk_2023)
- [III чемпионат Польши по спортивному ЧГК (2022)](#chgk_2022)
- [II чемпионат Польши по спортивному ЧГК (2019)](#chgk_2019)
- [I чемпионат Польши по спортивному ЧГК (2018)](#chgk_2018)


**VII чемпионат Польши по спортивному «Что? Где? Когда?»** прошёл 21–23 марта 2026 года в Варшаве. <a id="chgk_2026"></a>

Победитель: **[«Кринж без выходных» (Варшава)](https://rating.chgk.info/teams/85064)**
- Монина
- Юрий Разумов
- Владислава Плохих
- Юрий Яковлев
- Дмитрий Слободянюк
- Алексей Винокуров

Второе место заняла команда [Polish Space Marines](https://rating.chgk.info/teams/77174) (Краков). Третье место разделили команды [«1067»](https://rating.chgk.info/teams/10) (Варшава) и [«Просто чилим»](https://rating.chgk.info/teams/91508) (Вроцлав).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/13180). Фотографии с турнира можно посмотреть по [этой ссылке](https://drive.google.com/drive/folders/1hyIghXAiQE8VHUNebi3K1mAATArmeXVc). Больше информации о турнире — [на сайте чемпионата](https://4gk.pl/ochp), [в этом телеграм-канале](https://t.me/chgkpolska/113) и [здесь](https://t.me/chgknews/1403).

*[К оглавлению](#contents)*

---

**VI чемпионат Польши по спортивному «Что? Где? Когда?»** прошёл 5–6 апреля 2025 года в Варшаве. <a id="chgk_2025"></a>

Победитель: **[«Гимназия имени контркультурщика Юрия Яковлева» (Варшава)](https://rating.chgk.info/teams/85064)**
- Климентий Комиссаров
- Юрий Разумов
- Владислава Плохих
- Дарья Соловей
- Дмитрий Слободянюк
- Алексей Винокуров

Второе место заняла команда [«4:20»](https://rating.chgk.info/teams/86732) (Краков), третье — [«Самая большая лягушка»](https://rating.chgk.info/teams/86769) (Варшава).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11706). Фотографии с турнира можно посмотреть по [этой ссылке](https://drive.google.com/drive/folders/18jTDw_2wF5y_u3XAVTjruTWqty5mBlc9). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chgkpolska/62) и [здесь](https://t.me/chgknews/1101).

*[К оглавлению](#contents)*

---

**V чемпионат Польши по спортивному «Что? Где? Когда?»** прошёл 13–14 апреля 2024 года в Варшаве. <a id="chgk_2024"></a>

Победитель: **[Polish Space Marines (Краков)](https://rating.chgk.info/teams/77174)**
- Евгений Сибиряк
- Инна Семёнова
- Валерий Семёнов
- Надежда Лейчинская
- Сергей Демяненко
- Виктория Волкова

Второе место заняла команда [«Гимназия имени Кейси Легумины»](https://rating.chgk.info/teams/85064) (Варшава), третье — [WarSowiak](https://rating.chgk.info/teams/58672) (Варшава).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/10468). Фотографии с турнира можно посмотреть по [этой ссылке](https://t.me/polskastudent/4936). Больше информации о турнире — [в этом телеграм-канале](https://t.me/chgkpolska/20) и [здесь](https://t.me/chgknews/797).

*[К оглавлению](#contents)*

---

**IV чемпионат Польши по спортивному «Что? Где? Когда?»** прошёл 1–2 апреля 2023 года в Варшаве. <a id="chgk_2023"></a>

Победитель: **[«Гимназия имени прочитанного регламента» (Варшава)](https://rating.chgk.info/teams/85064)**
- Монина
- Юрий Разумов
- Владислава Плохих
- Дмитрий Слободянюк
- Павел Муха
- Алексей Винокуров

Второе место заняла команда [Polish Space Marines](https://rating.chgk.info/teams/77174) (Краков), третье — [«7:52»](https://rating.chgk.info/teams/55501) (Минск).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/8661). Фотографии с турнира можно посмотреть по [этой ссылке](https://www.facebook.com/media/set/?set=oa.3486871908212385&type=3). Больше информации о турнире — [в Facebook](https://www.facebook.com/events/905962520536562/?active_tab=discussion) и [здесь](https://t.me/chgknews/463).

*[К оглавлению](#contents)*

---

**III чемпионат Польши по спортивному «Что? Где? Когда?»** прошёл 23 июля 2022 года в Варшаве. <a id="chgk_2022"></a>

Победитель: **[Polish Space Marines (Краков)](https://rating.chgk.info/teams/77174)**
- Станислав Адаскевич
- Мария Завьялова
- Елена Гордынец
- Евгений Сибиряк
- Сергей Демяненко
- Виктория Волкова

Второе место заняла команда [«Есть желающие»](https://rating.chgk.info/teams/62709) (Вроцлав), третье — [«Клёк»](https://rating.chgk.info/teams/59514) (Варшава).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/8178). Больше информации о турнире — [здесь](https://t.me/chgknews/327).

*[К оглавлению](#contents)*

---

**II чемпионат Польши по спортивному «Что? Где? Когда?»** прошёл 18–19 мая 2019 года в Варшаве. <a id="chgk_2019"></a>

Победитель: **[«Глеб Шишкин» (Краков)](https://rating.chgk.info/teams/56081)**
- Елена Гордынец
- Ксения Накладова
- Владимир Кукарских
- Егор Игнатенков
- Сергей Демяненко
- Алексей Винокуров

Второе место заняла команда [«Большие люди»](https://rating.chgk.info/teams/56078) (Краков), третье — [«Есть желающие»](https://rating.chgk.info/teams/62709) (Вроцлав).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5484).

*[К оглавлению](#contents)*

---

**I чемпионат Польши по спортивному «Что? Где? Когда?»** прошёл 28–29 апреля 2018 года в Варшаве. <a id="chgk_2018"></a>

Победитель: **[«Глеб Шишкин» (Краков)](https://rating.chgk.info/teams/56081)**
- Елена Гордынец
- Андрей Руденко
- Дмитрий Слободянюк
- Владимир Кукарских
- Сергей Демяненко
- Алексей Винокуров

Второе место заняла команда [WarSowiak](https://rating.chgk.info/teams/58672) (Варшава), третье — [«Есть желающие»](https://rating.chgk.info/teams/62709) (Вроцлав).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4853).

*[К оглавлению](#contents)*

---

<div class="country-tab-end"></div>
