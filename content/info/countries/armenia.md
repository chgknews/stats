---
title: Армения
weight: 1
bookToC: false
---

# Армения

Чемпионаты Армении по спортивному ЧГК проводятся с 1994 года. Ниже можно увидеть статистику по всем призёрам — как командам, так и игрокам. Также в отдельных вкладках можно найти информацию о чемпионатах страны по той или иной дисциплине.

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-chgk" aria-selected="false">Турниры по ЧГК</button><button type="button" role="tab" data-tab="game-ssi" aria-selected="false">Турниры по ССИ</button><button type="button" role="tab" data-tab="missing-data" aria-selected="false">Нет данных</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th>Команда</th><th>Город</th><th>I</th><th>II</th><th>III</th><th>∑</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/1025">Двин (РПА-DAF / DAF / ДАФ)</a></td>
<td>Ереван</td>
<td>5</td>
<td>6</td>
<td>6</td>
<td>17</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/245">Айастан</a></td>
<td>Ереван</td>
<td>2</td>
<td>7</td>
<td>6</td>
<td>15</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/640">Перезагрузка (Перезагрузка-Орион)</a></td>
<td>Ереван</td>
<td>7</td>
<td>3</td>
<td>2</td>
<td>12</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/56664">Арагаст</a></td>
<td>Ереван</td>
<td>6</td>
<td>1</td>
<td>0</td>
<td>7</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/5141">НУИХ</a></td>
<td>Ереван</td>
<td>0</td>
<td>2</td>
<td>4</td>
<td>6</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/86520">Жуки-акробаты и паук-канатоходец</a></td>
<td>сборная</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/52916">Неловко</a></td>
<td>сборная</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/149">АССА</a></td>
<td>Ереван</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/103264">Арамазд — Григорян</a></td>
<td>Гюмри</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/29565">ЕрГМУ</a></td>
<td>Ереван</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/38741">Максфилд</a></td>
<td>Гюмри</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/35735">Факиры</a></td>
<td>Гюмри</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/103265">Арамазд — Элларян</a></td>
<td>Гюмри</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/29563">ДаФ (Команда Марка Григоряна)</a></td>
<td>Ереван</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/95189">Какие сладкие люди в Ереване</a></td>
<td>Ереван</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/30688">Армения-эрудит</a></td>
<td>Ереван</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/3301">Медикус (Немезис)</a></td>
<td>Ереван</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/26618">Орион</a></td>
<td>Шуши</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/51169">Орфей</a></td>
<td>Ереван</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/103266">Пресса</a></td>
<td>Ереван</td>
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
<td><a href="https://rating.chgk.info/player/29973">Павел Солахян</a></td>
<td>21</td>
<td>5</td>
<td>1</td>
<td>27</td>
<td>13</td>
<td>4</td>
<td>1</td>
<td>8</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1562">Арам Арутюнян</a></td>
<td>10</td>
<td>8</td>
<td>2</td>
<td>20</td>
<td>9</td>
<td>5</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/16154">Тигран Кочарян</a></td>
<td>8</td>
<td>4</td>
<td>5</td>
<td>17</td>
<td>7</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20345">Ева Махмурян</a></td>
<td>0</td>
<td>7</td>
<td>10</td>
<td>17</td>
<td>0</td>
<td>5</td>
<td>6</td>
<td>0</td>
<td>2</td>
<td>4</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19143">Тигран Магакян</a></td>
<td>4</td>
<td>6</td>
<td>4</td>
<td>14</td>
<td>3</td>
<td>6</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6708">Асмик Гаряка</a></td>
<td>4</td>
<td>6</td>
<td>4</td>
<td>14</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>3</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8118">Левон Григорян</a></td>
<td>3</td>
<td>6</td>
<td>4</td>
<td>13</td>
<td>3</td>
<td>6</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/658">Нора Аланакян</a></td>
<td>3</td>
<td>6</td>
<td>4</td>
<td>13</td>
<td>3</td>
<td>6</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22734">Левон Никогосян</a></td>
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
<td><a href="https://rating.chgk.info/player/278">Араик Аветисян</a></td>
<td>0</td>
<td>6</td>
<td>5</td>
<td>11</td>
<td>0</td>
<td>5</td>
<td>5</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/176">Сергей Абрамян</a></td>
<td>8</td>
<td>2</td>
<td>0</td>
<td>10</td>
<td>8</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6796">Аргишти Геворкян</a></td>
<td>3</td>
<td>3</td>
<td>4</td>
<td>10</td>
<td>2</td>
<td>2</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31349">Роберт Татоян</a></td>
<td>1</td>
<td>3</td>
<td>6</td>
<td>10</td>
<td>1</td>
<td>3</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19565">Ваагн Малоян</a></td>
<td>0</td>
<td>4</td>
<td>6</td>
<td>10</td>
<td>0</td>
<td>4</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12219">Евгения Иванова</a></td>
<td>8</td>
<td>1</td>
<td>0</td>
<td>9</td>
<td>8</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19811">Сурен Манукян</a></td>
<td>5</td>
<td>1</td>
<td>2</td>
<td>8</td>
<td>5</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/639">Арутюн Алавердян</a></td>
<td>1</td>
<td>3</td>
<td>4</td>
<td>8</td>
<td>1</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12915">Айк Казазян</a></td>
<td>6</td>
<td>0</td>
<td>1</td>
<td>7</td>
<td>6</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28255">Ваган Сардарян</a></td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>7</td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2033">Вардан Багирян</a></td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>7</td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28544">Маргар Седракян</a></td>
<td>4</td>
<td>0</td>
<td>2</td>
<td>6</td>
<td>4</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31378">Альгис Тваскис</a></td>
<td>3</td>
<td>3</td>
<td>0</td>
<td>6</td>
<td>3</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/49574">Самвел Хачатрян</a></td>
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
<td><a href="https://rating.chgk.info/player/61120">Артём Гукасян</a></td>
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
<td><a href="https://rating.chgk.info/player/29552">Степан Смбатян</a></td>
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
<td><a href="https://rating.chgk.info/player/30530">Александр Степанян</a></td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>5</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/24757">Артём Петросян</a></td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>5</td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34614">Ара Чарчян</a></td>
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
<td><a href="https://rating.chgk.info/player/19568">Арег Малхасян</a></td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>4</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/42837">Рачья Гумроян</a></td>
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
<td><a href="https://rating.chgk.info/player/31132">Арсен Тавадян</a></td>
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
<td><a href="https://rating.chgk.info/player/109746">Виген Ананян</a></td>
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
<td><a href="https://rating.chgk.info/player/33943">Гайк Хемчян</a></td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/96330">Наталья Комар</a></td>
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
<td><a href="https://rating.chgk.info/player/40118">Эдгар Маркосян</a></td>
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
<td><a href="https://rating.chgk.info/player/61094">Арутюн Арзуманян</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/195702">Давид Акопян</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/46976">Мансур Зиятдинов</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34476">Роман Цуркан</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/116424">Арина Далецкая</a></td>
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
<td><a href="https://rating.chgk.info/player/96039">Дмитрий Диденко</a></td>
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
<td><a href="https://rating.chgk.info/player/25121">Дмитрий Плотников</a></td>
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
<td><a href="https://rating.chgk.info/player/38168">Максим Карачун</a></td>
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
<td><a href="https://rating.chgk.info/player/31848">Александр Тобенгауз</a></td>
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
<td><a href="https://rating.chgk.info/player/6794">Альберт Геворкян</a></td>
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
<td><a href="https://rating.chgk.info/player/17203">Арам Кулиджанян</a></td>
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
<td><a href="https://rating.chgk.info/player/64613">Арсен Ааронян</a></td>
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
<td><a href="https://rating.chgk.info/player/8121">Марк Григорян</a></td>
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
<td><a href="https://rating.chgk.info/player/64623">Гурген Есаян</a></td>
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
<td><a href="https://rating.chgk.info/player/35889">Игорь Шевченко</a></td>
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
<td><a href="https://rating.chgk.info/player/101518">Евгений Марголин</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28275">Карен Саркисян</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/56486">Райганат Каримулаева</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/24850">Александр Печеный</a></td>
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
<td><a href="https://rating.chgk.info/player/60585">Анна Арцруни</a></td>
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
<td><a href="https://rating.chgk.info/player/31553">Ваге Тер-Минасян</a></td>
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
<td><a href="https://rating.chgk.info/player/87809">Виктория Вяземская</a></td>
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
<td><a href="https://rating.chgk.info/player/12773">Владимир Итыгин</a></td>
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
<td><a href="https://rating.chgk.info/player/60018">Левон Манукян</a></td>
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
<td><a href="https://rating.chgk.info/player/11853">Микаэл Золян</a></td>
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
<td><a href="https://rating.chgk.info/player/8131">Шант Григорян</a></td>
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
<td><a href="https://rating.chgk.info/player/60584">Эмиль Манукян</a></td>
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
<td><a href="https://rating.chgk.info/player/113357">Алексей Овчинников</a></td>
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
<td><a href="https://rating.chgk.info/player/115151">Андрей Маврин</a></td>
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
<td><a href="https://rating.chgk.info/player/2026">Арсен Багдатян</a></td>
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
<td><a href="https://rating.chgk.info/player/20657">Ашот Мельян</a></td>
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
<td><a href="https://rating.chgk.info/player/28440">Екатерина Свешникова</a></td>
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
<td><a href="https://rating.chgk.info/player/33293">Игорь Философов</a></td>
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
<td><a href="https://rating.chgk.info/player/113330">Константин Шведов</a></td>
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
<td><a href="https://rating.chgk.info/player/13631">Мария Карпова</a></td>
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
<td><a href="https://rating.chgk.info/player/136830">Михаил Московченко</a></td>
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
<td><a href="https://rating.chgk.info/player/32901">Наиль Фарукшин</a></td>
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
<td><a href="https://rating.chgk.info/player/33624">Ренат Хайбуллин</a></td>
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
<td><a href="https://rating.chgk.info/player/119877">Светлана Смолоногова</a></td>
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
<td><a href="https://rating.chgk.info/player/31493">Сергей Терентьев</a></td>
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
<td><a href="https://rating.chgk.info/player/107372">Юлия Маврина</a></td>
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
<td>Авет Керопян</td>
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
<td><a href="https://rating.chgk.info/player/209">Арман Авакян</a></td>
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
<td><a href="https://rating.chgk.info/player/1695">Армен Аствацатрян</a></td>
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
<td><a href="https://rating.chgk.info/player/8110">Артём Григорян</a></td>
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
<td><a href="https://rating.chgk.info/player/30152">Артём Сорожкин</a></td>
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
<td><a href="https://rating.chgk.info/player/97663">Астхик Петросян</a></td>
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
<td><a href="https://rating.chgk.info/player/60017">Гагик Саакян</a></td>
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
<td><a href="https://rating.chgk.info/player/8667">Гайк Гюзалян</a></td>
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
<td><a href="https://rating.chgk.info/player/148624">Дамир Маликов</a></td>
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
<td><a href="https://rating.chgk.info/player/30236">Данила Софинский</a></td>
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
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/50761">Ирина Вопян</a></td>
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
<td><a href="https://rating.chgk.info/player/9235">Маргарита Джагацпанян</a></td>
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
<td><a href="https://rating.chgk.info/player/131934">Мери Арутюнян</a></td>
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
<td><a href="https://rating.chgk.info/player/60016">Месроп Акопян</a></td>
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
<td><a href="https://rating.chgk.info/player/4763">Михаил Быстров</a></td>
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
<td><a href="https://rating.chgk.info/player/50763">Ованес Ованесян</a></td>
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
<td><a href="https://rating.chgk.info/player/186">Хачатур Аброян</a></td>
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
<td><a href="https://rating.chgk.info/player/31998">Григор Топушян</a></td>
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
</tr>
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-chgk"></div>

<a id="game-chgk"></a><a id="chgk_contents" name="chgk_contents"></a>

- [XXVII чемпионат Армении по спортивному ЧГК (2026)](#chgk_2026)
- [XXVI чемпионат Армении по спортивному ЧГК (2025)](#chgk_2025)
- [XXV чемпионат Армении по спортивному ЧГК (2024)](#chgk_2024)
- [XXIV чемпионат Армении по спортивному ЧГК (2023)](#chgk_2023)
- [XXIII чемпионат Армении по спортивному ЧГК (2022)](#chgk_2022)
- [XXII чемпионат Армении по спортивному ЧГК (2021)](#chgk_2021)
- [XXI чемпионат Армении по спортивному ЧГК (2019)](#chgk_2019)
- [Открытый чемпионат Армении (2018, на армянском языке)](#chgk_2018)
- [XX чемпионат Армении по спортивному ЧГК (2018)](#chgk_2018)
- [XIX чемпионат Армении по спортивному ЧГК (2017)](#chgk_2017)
- [XVIII чемпионат Армении по спортивному ЧГК (2016)](#chgk_2016)
- [XVII чемпионат Армении по спортивному ЧГК (2015)](#chgk_2015)
- [XVI чемпионат Армении по спортивному ЧГК (2014)](#chgk_2014)
- [XV чемпионат Армении по спортивному ЧГК (2013)](#chgk_2013)
- [XIV чемпионат Армении по спортивному ЧГК (2012)](#chgk_2012)
- [XIII чемпионат Армении по спортивному ЧГК (2011)](#chgk_2011)
- [XII чемпионат Армении по спортивному ЧГК (2010)](#chgk_2010)
- [XI чемпионат Армении по спортивному ЧГК (2009)](#chgk_2009)
- [X чемпионат Армении по спортивному ЧГК (2008)](#chgk_2008)
- [IX чемпионат Армении по спортивному ЧГК (2007)](#chgk_2007)
- [VIII чемпионат Армении по спортивному ЧГК (2006)](#chgk_2006)
- [VII чемпионат Армении по спортивному ЧГК (2005)](#chgk_2005)
- [V чемпионат Армении по спортивному ЧГК (2003)](#chgk_2003)
- [IV чемпионат Армении по спортивному ЧГК (2001)](#chgk_2001)
- [III чемпионат Армении по спортивному ЧГК (1998)](#chgk_1998)
- [II чемпионат Армении по спортивному ЧГК (1995)](#chgk_1995)
- [I чемпионат Армении по спортивному ЧГК (1994)](#chgk_1994)


**XXVII чемпионат Армении по спортивному «Что? Где? Когда?»** пройдёт 12 сентября 2026 года в Гюмри. <a name="chgk_2026"></a>

Больше информации о турнире — [в анонсе](https://telegram.me/ChgkgamesArmenia/471).


*[К оглавлению](#chgk_contents)*

---

**XXVI чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 15 июня 2025 года в Ереване. <a name="chgk_2025"></a>

Победитель: **[«Жуки-акробаты и паук-канатоходец» (сборная)](https://rating.chgk.info/teams/86520)**
- Арина Далецкая
- Наталья Комар
- Дмитрий Диденко
- Максим Карачун
- Дмитрий Плотников
- Александр Печеный

Второе место заняла команда [«Арагаст»](https://rating.chgk.info/teams/56664) (Ереван), третье — [«Неловко»](https://rating.chgk.info/teams/52916) (сборная).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12169).


*[К оглавлению](#chgk_contents)*

---

**XXV чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 26 мая 2024 года в Ереване. <a name="chgk_2024"></a>

Победитель: **[«Жуки-акробаты и паук-канатоходец» (сборная)](https://rating.chgk.info/teams/86520)**
- Арина Далецкая
- Наталья Комар
- Дмитрий Диденко
- Максим Карачун
- Дмитрий Плотников

Второе место заняла команда [«Какие сладкие люди в Ереване»](https://rating.chgk.info/teams/95189) (Ереван), третье — [«Неловко»](https://rating.chgk.info/teams/52916) (сборная).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/10763).


*[К оглавлению](#chgk_contents)*

---

**XXIV чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 28 мая 2023 года в Гюмри. <a name="chgk_2023"></a>

Победитель: **[«Арагаст» (Ереван)](https://rating.chgk.info/teams/56664)**
- Рачья Гумроян
- Александр Тобенгауз
- Павел Солахян
- Арам Кулиджанян
- Арам Арутюнян
- Сергей Абрамян

Второе место заняла команда [«Жуки-акробаты и паук-канатоходец»](https://rating.chgk.info/teams/86520) (сборная), третье — [«Неловко»](https://rating.chgk.info/teams/52916) (сборная).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/9379).


*[К оглавлению](#chgk_contents)*

---

**XXIII чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 17 июля 2022 года в Ереване. <a name="chgk_2022"></a>

Победитель: **[«Арагаст» (Ереван)](https://rating.chgk.info/teams/56664)**
- Виктория Вяземская
- Рачья Гумроян
- Павел Солахян
- Арег Малхасян
- Евгения Иванова
- Сергей Абрамян

Второе место заняла команда [«Айастан»](https://rating.chgk.info/teams/245) (Ереван). Третье место разделили команды [«Двин»](https://rating.chgk.info/teams/1025) (Ереван) и [«НУИХ»](https://rating.chgk.info/teams/5141) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/8211).


*[К оглавлению](#chgk_contents)*

---

**XXII чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 26 сентября 2021 года в Ереване. <a name="chgk_2021"></a>

Победитель: **[«Арагаст» (Ереван)](https://rating.chgk.info/teams/56664)**
- Рачья Гумроян
- Арсен Тавадян
- Павел Солахян
- Арег Малхасян
- Евгения Иванова
- Сергей Абрамян

Второе место заняла команда [«НУИХ»](https://rating.chgk.info/teams/5141) (Ереван), третье — [«Айастан»](https://rating.chgk.info/teams/245) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/7483).


*[К оглавлению](#chgk_contents)*

---

**XXI чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 7–8 сентября 2019 года в Ереване. <a name="chgk_2019"></a>

Победитель: **[«Арагаст» (Ереван)](https://rating.chgk.info/teams/56664)**
- Павел Солахян
- Арег Малхасян
- Владимир Итыгин
- Евгения Иванова
- Арам Арутюнян
- Сергей Абрамян

Второе место заняла команда [«Двин»](https://rating.chgk.info/teams/1025) (Ереван), третье — [«НУИХ»](https://rating.chgk.info/teams/5141) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5911).


*[К оглавлению](#chgk_contents)*

---

**Открытый чемпионат Армении** прошёл 21 сентября 2018 года в Ереване. Вопросы задавались на армянском языке. <a name="chgk_2018"></a>

Победитель: **[«Арагаст» (Ереван)](https://rating.chgk.info/teams/56664)**
- Павел Солахян
- Арам Кулиджанян
- Евгения Иванова
- Левон Григорян
- Арам Арутюнян
- Сергей Абрамян

Второе место заняла команда [«НУИХ»](https://rating.chgk.info/teams/5141) (Ереван), третье — [«Anfield»](https://rating.chgk.info/teams/38791) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5177).

*Турнир не учитывается в общей медальной статистике.*


*[К оглавлению](#chgk_contents)*

---

**XX чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 15 июля 2018 года в Гюмри. <a name="chgk_2018"></a>

Победитель: **[«Арагаст» (Ереван)](https://rating.chgk.info/teams/56664)**
- Павел Солахян
- Арег Малхасян
- Евгения Иванова
- Вардан Багирян
- Арам Арутюнян
- Сергей Абрамян

Второе место заняла команда [«Двин»](https://rating.chgk.info/teams/1025) (Ереван), третье — [«НУИХ»](https://rating.chgk.info/teams/5141) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5075).


*[К оглавлению](#chgk_contents)*

---

**XIX чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 9 июля 2017 года в Ереване. <a name="chgk_2017"></a>

Победитель: **[«Арагаст» (Ереван)](https://rating.chgk.info/teams/56664)**
- Арсен Ааронян
- Павел Солахян
- Евгения Иванова
- Арам Арутюнян
- Сергей Абрамян

Второе место заняла команда [«Двин»](https://rating.chgk.info/teams/1025) (Ереван), третье — [«НУИХ»](https://rating.chgk.info/teams/5141) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4446).


*[К оглавлению](#chgk_contents)*

---

**XVIII чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 31 июля 2016 года в Ереване. <a name="chgk_2016"></a>

Победитель: **[«Перезагрузка» (Ереван)](https://rating.chgk.info/teams/640)**
- Павел Солахян
- Маргар Седракян
- Тигран Кочарян
- Айк Казазян
- Евгения Иванова
- Сергей Абрамян

Второе место заняла команда [«НУИХ»](https://rating.chgk.info/teams/5141) (Ереван), третье — [«Айастан»](https://rating.chgk.info/teams/245) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3914), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/6422).


*[К оглавлению](#chgk_contents)*

---

**XVII чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 12 июля 2015 года в Гюмри. <a name="chgk_2015"></a>

Победитель: **[«Перезагрузка» (Ереван)](https://rating.chgk.info/teams/640)**
- Павел Солахян
- Маргар Седракян
- Тигран Кочарян
- Айк Казазян
- Евгения Иванова
- Сергей Абрамян

Второе место заняла команда [«Айастан»](https://rating.chgk.info/teams/245) (Ереван), третье — [«ДАФ»](https://rating.chgk.info/teams/1025) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3429), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/610).


*[К оглавлению](#chgk_contents)*

---

**XVI чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 21 июня 2014 года в Ереване. <a name="chgk_2014"></a>

Победитель: **[«Перезагрузка» (Ереван)](https://rating.chgk.info/teams/640)**
- Павел Солахян
- Сурен Манукян
- Тигран Кочарян
- Айк Казазян
- Евгения Иванова
- Арам Арутюнян

Второе место заняла команда [«Айастан»](https://rating.chgk.info/teams/245) (Ереван), третье — [«ДАФ»](https://rating.chgk.info/teams/1025) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2903), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/615).


*[К оглавлению](#chgk_contents)*

---

**XV чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 20 июля 2013 года в Ереване. <a name="chgk_2013"></a>

Победитель: **[«Перезагрузка» (Ереван)](https://rating.chgk.info/teams/640)**
- Павел Солахян
- Маргар Седракян
- Сурен Манукян
- Тигран Кочарян
- Айк Казазян
- Арам Арутюнян

Второе место заняла команда [«Айастан»](https://rating.chgk.info/teams/245) (Ереван), третье — [«ДАФ»](https://rating.chgk.info/teams/1025) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2399), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/2641).


*[К оглавлению](#chgk_contents)*

---

**XIV чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 30 июня 2012 года в Гюмри. <a name="chgk_2012"></a>

Победитель: **[«Перезагрузка» (Ереван)](https://rating.chgk.info/teams/640)**
- Павел Солахян
- Маргар Седракян
- Сурен Манукян
- Тигран Кочарян
- Айк Казазян
- Арам Арутюнян

Второе место заняла команда [«ДАФ»](https://rating.chgk.info/teams/1025) (Ереван), третье — [«Айастан»](https://rating.chgk.info/teams/245) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2134), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/2622).


*[К оглавлению](#chgk_contents)*

---

**XIII чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 11 июня 2011 года в Ереване. <a name="chgk_2011"></a>

Победитель: **[«Перезагрузка» (Ереван)](https://rating.chgk.info/teams/640)**
- Павел Солахян
- Ваган Сардарян
- Сурен Манукян
- Тигран Кочарян
- Айк Казазян
- Арам Арутюнян

Второе место заняла команда [«Айастан»](https://rating.chgk.info/teams/245) (Ереван), третье — [«ДАФ»](https://rating.chgk.info/teams/1025) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1852), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3248).


*[К оглавлению](#chgk_contents)*

---

**XII чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 29 мая 2010 года в Степанакерте. <a name="chgk_2010"></a>

Победитель: **[«Перезагрузка» (Ереван)](https://rating.chgk.info/teams/640)**
- Павел Солахян
- Ваган Сардарян
- Сурен Манукян
- Тигран Кочарян
- Вардан Багирян
- Арам Арутюнян

Второе место заняла команда [«ДАФ»](https://rating.chgk.info/teams/1025) (Ереван), третье — [«Айастан»](https://rating.chgk.info/teams/245) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/675), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3249).


*[К оглавлению](#chgk_contents)*

---

**XI чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 29 мая 2009 года в Ереване. <a name="chgk_2009"></a>

Победитель: **[«ДАФ» (Ереван)](https://rating.chgk.info/teams/1025)**
- Альгис Тваскис
- Левон Никогосян
- Тигран Магакян
- Левон Григорян
- Асмик Гаряка
- Нора Аланакян

Второе место заняла команда [«Перезагрузка»](https://rating.chgk.info/teams/640) (Ереван), третье — [«Айастан»](https://rating.chgk.info/teams/245) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/487), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4303).


*[К оглавлению](#chgk_contents)*

---

**X чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 29–30 мая 2008 года в Ереване. <a name="chgk_2008"></a>

Победитель: **[«ДАФ» (Ереван)](https://rating.chgk.info/teams/1025)**
- Альгис Тваскис
- Левон Никогосян
- Тигран Магакян
- Левон Григорян
- Асмик Гаряка
- Нора Аланакян

Второе место заняла команда [«Перезагрузка»](https://rating.chgk.info/teams/640) (Ереван), третье — [«Айастан»](https://rating.chgk.info/teams/245) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/360), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4717).


*[К оглавлению](#chgk_contents)*

---

**IX чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 9 июня 2007 года в Ереване. <a name="chgk_2007"></a>

Победитель: **[«DAF» (Ереван)](https://rating.chgk.info/teams/1025)**

*Состав команды [«DAF»](https://rating.chgk.info/teams/1025) (Ереван) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Айастан»](https://rating.chgk.info/teams/245) (Ереван). Третье место разделили команды [«Перезагрузка»](https://rating.chgk.info/teams/640) (Ереван) и [«АССА»](https://rating.chgk.info/teams/149) (Ереван). Больше информации о турнире — [здесь](https://chgk-am.livejournal.com/43906.html).


*[К оглавлению](#chgk_contents)*

---

**VIII чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 4 июня 2006 года в Ереване. <a name="chgk_2006"></a>

Победитель: **[«DAF» (Ереван)](https://rating.chgk.info/teams/1025)**

*Состав команды [«DAF»](https://rating.chgk.info/teams/1025) (Ереван) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Айастан»](https://rating.chgk.info/teams/245) (Ереван). Третье место разделили команды [«АССА»](https://rating.chgk.info/teams/149) (Ереван) и [«Перезагрузка-Орион»](https://rating.chgk.info/teams/640) (Ереван).


*[К оглавлению](#chgk_contents)*

---

**VII чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 18 июня 2005 года в Ереване. <a name="chgk_2005"></a>

Победитель: **[«РПА-DAF» (Ереван)](https://rating.chgk.info/teams/1025)**
- Альгис Тваскис
- Левон Никогосян
- Тигран Магакян
- Левон Григорян
- Асмик Гаряка
- Нора Аланакян

Второе место заняла команда [«Перезагрузка»](https://rating.chgk.info/teams/640) (Ереван), третье — [«Орион»](https://rating.chgk.info/teams/26618) (Шуши).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/108).


*[К оглавлению](#chgk_contents)*

---

**V чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 8 марта 2003 года в Ереване. <a name="chgk_2003"></a>

Победитель: **[«Айастан» (Ереван)](https://rating.chgk.info/teams/245)**
- Самвел Хачатрян
- Роберт Татоян
- Ваган Сардарян
- Аргишти Геворкян
- Альберт Геворкян
- Вардан Багирян

Второе место заняла команда [«РПА-DAF»](https://rating.chgk.info/teams/1025) (Ереван), третье — [«Медикус»](https://rating.chgk.info/teams/3301) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1347).


*[К оглавлению](#chgk_contents)*

---

**IV чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 22 декабря 2001 года в Ереване. <a name="chgk_2001"></a>

Победитель: **[«Айастан» (Ереван)](https://rating.chgk.info/teams/245)**
- Аргишти Геворкян

Второе место заняла команда [«ДаФ»](https://rating.chgk.info/teams/29563) (Ереван), третье — [«Армения-эрудит»](https://rating.chgk.info/teams/30688) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1223).


*[К оглавлению](#chgk_contents)*

---

**III чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 23 октября 1998 года в Ереване. <a name="chgk_1998"></a>

Первое место разделили команды [«ЕрГМУ»](https://rating.chgk.info/teams/29565) (Ереван) и [«Максфилд»](https://rating.chgk.info/teams/38741) (Гюмри). Состав команды [«ЕрГМУ»](https://rating.chgk.info/teams/29565):
- Анна Арцруни
- Эмиль Манукян
- Левон Манукян
- Ваге Тер-Минасян
- Микаэл Золян
- Арутюн Алавердян

*Состав команды [«Максфилд»](https://rating.chgk.info/teams/38741) (Гюмри) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Третье место разделили команды [«Двин»](https://rating.chgk.info/teams/1025) (Ереван) и [«Орфей»](https://rating.chgk.info/teams/51169) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1740).


*[К оглавлению](#chgk_contents)*

---

**II чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 4–5 октября 1995 года в Ереване. <a name="chgk_1995"></a>

Победитель: **[«Арамазд — Григорян» (Гюмри)](https://rating.chgk.info/teams/103264)**
- Шант Григорян

Второе место заняла команда [«Арамазд — Элларян»](https://rating.chgk.info/teams/103265) (Гюмри), третье — [«Пресса»](https://rating.chgk.info/teams/103266) (Ереван).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11561). Больше информации о турнире — [в Летописи](http://letopis.chgk.info/199511Erevan.html).


*[К оглавлению](#chgk_contents)*

---

**I чемпионат Армении по спортивному «Что? Где? Когда?»** прошёл 24–25 декабря 1994 года в Ереване. <a name="chgk_1994"></a>

Победитель: **[«Факиры» (Гюмри)](https://rating.chgk.info/teams/35735)**

*Состав команды [«Факиры»](https://rating.chgk.info/teams/35735) (Гюмри) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*
 Больше информации о турнире — [в Летописи](http://letopis.chgk.info/199412Yerevan.html).


*[К оглавлению](#chgk_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ssi"></div>

<a id="game-ssi"></a><a id="ssi_contents" name="ssi_contents"></a>

- [XVII чемпионат Армении по ССИ (2019)](#ssi_2019)
- [XVI чемпионат Армении по ССИ (2018)](#ssi_2018)
- [XV чемпионат Армении по ССИ (2017)](#ssi_2017)
- [XIV чемпионат Армении по ССИ (2016)](#ssi_2016)
- [XIII чемпионат Армении по ССИ (2015)](#ssi_2015)
- [IX чемпионат Армении по ССИ (2011)](#ssi_2011)
- [VIII чемпионат Армении по ССИ (2010)](#ssi_2010)
- [VII чемпионат Армении по ССИ (2009)](#ssi_2009)
- [VI чемпионат Армении по ССИ (2008)](#ssi_2008)
- [V чемпионат Армении по ССИ (2007)](#ssi_2007)
- [IV чемпионат Армении по ССИ (2006)](#ssi_2006)
- [III чемпионат Армении по ССИ (2005)](#ssi_2005)
- [II чемпионат Армении по ССИ (2004)](#ssi_2004)
- [I чемпионат Армении по ССИ (2003)](#ssi_2003)


**XVII чемпионат Армении по спортивной «Своей игре»** прошёл 2 ноября 2019 года в Ереване. <a name="ssi_2019"></a>

Победитель: **[Павел Солахян](https://rating.chgk.info/player/29973)**

Второе место занял [Ева Махмурян](https://rating.chgk.info/player/20345), третье — [Тигран Кочарян](https://rating.chgk.info/player/16154).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1hnOi5X2Xx86EEyO6ABmkQzfouK5WSD6NKU2dF-yTRsc/edit?gid=1329653126#gid=1329653126).


*[К оглавлению](#ssi_contents)*

---

**XVI чемпионат Армении по спортивной «Своей игре»** прошёл 30 июня 2018 года в Ереване. <a name="ssi_2018"></a>

Победитель: **[Павел Солахян](https://rating.chgk.info/player/29973)**

Второе место заняла [Ева Махмурян](https://rating.chgk.info/player/20345), третье — [Тигран Магакян](https://rating.chgk.info/player/19143).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1hnOi5X2Xx86EEyO6ABmkQzfouK5WSD6NKU2dF-yTRsc/edit?gid=2043986205#gid=2043986205).


*[К оглавлению](#ssi_contents)*

---

**XV чемпионат Армении по спортивной «Своей игре»** пройдёт в Ереване. <a name="ssi_2017"></a>

Победитель: **[Павел Солахян](https://rating.chgk.info/player/29973)**

Второе место занял [Арам Арутюнян](https://rating.chgk.info/player/1562), третье — [Ева Махмурян](https://rating.chgk.info/player/20345).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1hnOi5X2Xx86EEyO6ABmkQzfouK5WSD6NKU2dF-yTRsc/edit?gid=1306338601#gid=1306338601).


*[К оглавлению](#ssi_contents)*

---

**XIV чемпионат Армении по спортивной «Своей игре»** прошёл 11 июня 2016 года в Ереване. <a name="ssi_2016"></a>

Победитель: **[Павел Солахян](https://rating.chgk.info/player/29973)**

Второе место занял [Арам Арутюнян](https://rating.chgk.info/player/1562), третье — [Ева Махмурян](https://rating.chgk.info/player/20345).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1hnOi5X2Xx86EEyO6ABmkQzfouK5WSD6NKU2dF-yTRsc/edit?gid=1103250116#gid=1103250116).


*[К оглавлению](#ssi_contents)*

---

**XIII чемпионат Армении по спортивной «Своей игре»** пройдёт в Ереване. <a name="ssi_2015"></a>

Победитель: **[Павел Солахян](https://rating.chgk.info/player/29973)**

Второе место заняла [Асмик Гаряка](https://rating.chgk.info/player/6708), третье — [Тигран Кочарян](https://rating.chgk.info/player/16154).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1hnOi5X2Xx86EEyO6ABmkQzfouK5WSD6NKU2dF-yTRsc/edit?gid=398184109#gid=398184109).


*[К оглавлению](#ssi_contents)*

---

**IX чемпионат Армении по спортивной «Своей игре»** прошёл 23–24 июля 2011 года в Ереване. <a name="ssi_2011"></a>

Победитель: **[Павел Солахян](https://rating.chgk.info/player/29973)**

Второе место заняла [Асмик Гаряка](https://rating.chgk.info/player/6708), третье — [Тигран Кочарян](https://rating.chgk.info/player/16154).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/u/0/d/1vBT7ZBCCtypSmzjfaMOJO4jomgdB7uSXGYJRAYkjSQs/pub?hl=en_US&pli=1&hl=en_US&hl=en_US&gid=4&pli=1). Больше информации о турнире — [здесь](https://svoja-igra-am.livejournal.com/111792.html).


*[К оглавлению](#ssi_contents)*

---

**VIII чемпионат Армении по спортивной «Своей игре»** прошёл 18 июля 2010 года в Ереване. <a name="ssi_2010"></a>

Победитель: **[Павел Солахян](https://rating.chgk.info/player/29973)**

Второе место занял [Араик Аветисян](https://rating.chgk.info/player/278), третье — [Арам Арутюнян](https://rating.chgk.info/player/1562). Больше информации о турнире — [здесь](https://svoja-igra-am.livejournal.com/83932.html).


*[К оглавлению](#ssi_contents)*

---

**VII чемпионат Армении по спортивной «Своей игре»** прошёл 12 июля 2009 года в Ереване. <a name="ssi_2009"></a>

Победитель: **[Арам Арутюнян](https://rating.chgk.info/player/1562)**

Второе место занял [Александр Степанян](https://rating.chgk.info/player/30530), третье — [Григор Топушян](https://rating.chgk.info/player/31998). Больше информации о турнире — [здесь](https://svoja-igra-am.livejournal.com/54138.html).


*[К оглавлению](#ssi_contents)*

---

**VI чемпионат Армении по спортивной «Своей игре»** прошёл 6 июля 2008 года в Ереване. <a name="ssi_2008"></a>

Победитель: **[Павел Солахян](https://rating.chgk.info/player/29973)**

Второе место занял [Арам Арутюнян](https://rating.chgk.info/player/1562), третье — [Ева Махмурян](https://rating.chgk.info/player/20345). Больше информации о турнире — [здесь](https://svoja-igra-am.livejournal.com/19867.html).


*[К оглавлению](#ssi_contents)*

---

**V чемпионат Армении по спортивной «Своей игре»** прошёл 15 июля 2007 года в Ереване. <a name="ssi_2007"></a>

Победитель: **[Александр Степанян](https://rating.chgk.info/player/30530)**

Второе место заняла [Асмик Гаряка](https://rating.chgk.info/player/6708), третье — [Ева Махмурян](https://rating.chgk.info/player/20345). Больше информации о турнире — [здесь](https://chgk-am.livejournal.com/52069.html).


*[К оглавлению](#ssi_contents)*

---

**IV чемпионат Армении по спортивной «Своей игре»** пройдёт в Ереване. <a name="ssi_2006"></a>

Победитель: **[Тигран Кочарян](https://rating.chgk.info/player/16154)**

*На этом турнире часть призёров неизвестна. Если вы что-то о них знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*


*[К оглавлению](#ssi_contents)*

---

**III чемпионат Армении по спортивной «Своей игре»** пройдёт в Ереване. <a name="ssi_2005"></a>

Победитель: **[Аргишти Геворкян](https://rating.chgk.info/player/6796)**

Второе место занял [Павел Солахян](https://rating.chgk.info/player/29973).

*На этом турнире часть призёров неизвестна. Если вы что-то о них знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*


*[К оглавлению](#ssi_contents)*

---

**II чемпионат Армении по спортивной «Своей игре»** пройдёт в Ереване. <a name="ssi_2004"></a>

Победитель: **[Асмик Гаряка](https://rating.chgk.info/player/6708)**

*На этом турнире часть призёров неизвестна. Если вы что-то о них знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*


*[К оглавлению](#ssi_contents)*

---

**I чемпионат Армении по спортивной «Своей игре»** прошёл 23 февраля 2003 года в Ереване. <a name="ssi_2003"></a>

Победитель: **[Тигран Магакян](https://rating.chgk.info/player/19143)**

Второе место занял [Аргишти Геворкян](https://rating.chgk.info/player/6796), третье — [Асмик Гаряка](https://rating.chgk.info/player/6708). Больше информации о турнире — [в Летописи](http://news.chgk.info/200302ErevanJeop.html).


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
<tr><td>2017</td><td>XV чемпионат Армении по ССИ</td><td>неизвестна точная дата проведения.</td></tr>
<tr><td>2015</td><td>XIII чемпионат Армении по ССИ</td><td>неизвестна точная дата проведения.</td></tr>
<tr><td>2013</td><td><a href="https://rating.chgk.info/tournament/2399">XV чемпионат Армении по ЧГК</a></td><td>неизвестны составы обладателей второго и третьего мест.</td></tr>
<tr><td>2007</td><td>IX чемпионат Армении по ЧГК</td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2006</td><td>VIII чемпионат Армении по ЧГК</td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2006</td><td>IV чемпионат Армении по ССИ</td><td>неизвестны обладатели второго и третьего мест, точная дата проведения турнира.</td></tr>
<tr><td>2005</td><td>III чемпионат Армении по ССИ</td><td>неизвестны обладатель третьего места, точная дата проведения турнира.</td></tr>
<tr><td>2004</td><td>II чемпионат Армении по ССИ</td><td>неизвестны обладатели второго и третьего мест, точная дата проведения турнира.</td></tr>
<tr><td>2001</td><td><a href="https://rating.chgk.info/tournament/1223">IV чемпионат Армении по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>1998</td><td><a href="https://rating.chgk.info/tournament/1740">III чемпионат Армении по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>1995</td><td><a href="https://rating.chgk.info/tournament/11561">II чемпионат Армении по ЧГК</a></td><td>неизвестны составы обладателей второго и третьего мест.</td></tr>
<tr><td>1994</td><td>I чемпионат Армении по ЧГК</td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
