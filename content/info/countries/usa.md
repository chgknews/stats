---
title: США
weight: 1
bookToC: false
---

# США

Чемпионаты США проводятся с 1997 года.

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
<nav class="country-tab-bar" role="tablist"><button type="button" role="tab" class="is-active" data-tab="teams" aria-selected="true">Команды</button><button type="button" role="tab" data-tab="players" aria-selected="false">Игроки</button><button type="button" role="tab" data-tab="game-chgk" aria-selected="false">Турниры по ЧГК</button><button type="button" role="tab" data-tab="game-brain" aria-selected="false">Турниры по БР</button><button type="button" role="tab" data-tab="game-ssi" aria-selected="false">Турниры по ССИ</button><button type="button" role="tab" data-tab="missing-data" aria-selected="false">Проблемы</button><button type="button" role="tab" data-tab="sources" aria-selected="false">Источники и благодарности</button></nav>
<div class="country-tab-hide-until-ready"></div>
<div class="country-tab-start" data-tab="teams"></div>

<a id="teams"></a>

<table>
<thead>
<tr><th rowspan="2">Команда</th><th rowspan="2">Город</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">ЧГК</th><th colspan="3" style="text-align:center">БР</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/teams/1733">Суббота 13</a></td>
<td>Нью-Йорк</td>
<td>12</td>
<td>12</td>
<td>4</td>
<td>28</td>
<td>7</td>
<td>7</td>
<td>4</td>
<td>5</td>
<td>5</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/216">Инк</a></td>
<td>Пало-Альто</td>
<td>9</td>
<td>7</td>
<td>6</td>
<td>22</td>
<td>6</td>
<td>6</td>
<td>4</td>
<td>3</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/446">Тормоза</a></td>
<td>Пало-Альто</td>
<td>5</td>
<td>5</td>
<td>10</td>
<td>20</td>
<td>3</td>
<td>5</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>5</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/38917">Кузинатра</a></td>
<td>Сиэтл</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>9</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/51796">Заливная</a></td>
<td>Пало-Альто</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>5</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/37611">Аппалачи</a></td>
<td>Вашингтон</td>
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
<td><a href="https://rating.chgk.info/teams/7542">Vademecum (Гексаэдр)</a></td>
<td>Бостон</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/1181">Лямбда</a></td>
<td>Нью-Йорк</td>
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
<td><a href="https://rating.chgk.info/teams/46750">Весёлые монахи</a></td>
<td>Пало-Альто</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/105990">Надо подкачаться</a></td>
<td>сборная</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/271">Саша и медведи</a></td>
<td>Торонто</td>
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
<td><a href="https://rating.chgk.info/teams/1966">Веретено</a></td>
<td>Торонто</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/teams/799">Почти соседи</a></td>
<td>Нью-Йорк</td>
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
<td><a href="https://rating.chgk.info/teams/138">Нонсенс</a></td>
<td>Пало-Альто</td>
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
<td><a href="https://rating.chgk.info/teams/69931">АбВер: операция Туда, блин!</a></td>
<td>Торонто</td>
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
<td><a href="https://rating.chgk.info/teams/29938">Спрайт</a></td>
<td>Нью-Йорк</td>
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
<td><a href="https://rating.chgk.info/teams/231">Стоп-сигнал</a></td>
<td>Пало-Альто</td>
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
<td><a href="https://rating.chgk.info/teams/365">Вестимо</a></td>
<td>Торонто</td>
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
<td><a href="https://rating.chgk.info/teams/28217">Выше плинтуса</a></td>
<td>Чикаго</td>
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
<td><a href="https://rating.chgk.info/teams/55189">MW</a></td>
<td>Пало-Альто</td>
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
<td><a href="https://rating.chgk.info/teams/4144">Вилладжеры</a></td>
<td>Нью-Йорк</td>
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
<td><a href="https://rating.chgk.info/teams/32243">Чикаго</a></td>
<td>Чикаго</td>
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
<td><a href="https://rating.chgk.info/teams/28288">Американская солянка</a></td>
<td>сборная</td>
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
<td><a href="https://rating.chgk.info/teams/1099">Дом</a></td>
<td>Бостон</td>
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
<td><a href="https://rating.chgk.info/teams/79631">НИИЧАВО</a></td>
<td>Нью-Йорк</td>
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
<td><a href="https://rating.chgk.info/teams/44622">Соседи сверху</a></td>
<td>сборная</td>
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
<td><a href="https://rating.chgk.info/teams/2378">Ботва</a></td>
<td>Пало-Альто</td>
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
<td><a href="https://rating.chgk.info/teams/449">Вечно живые</a></td>
<td>Пало-Альто</td>
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
<td><a href="https://rating.chgk.info/teams/39739">ВС+</a></td>
<td>Нью-Йорк</td>
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
<td><a href="https://rating.chgk.info/teams/39746">Матильда</a></td>
<td>Нью-Йорк</td>
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
<td><a href="https://rating.chgk.info/teams/29939">Палата №6</a></td>
<td>сборная</td>
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
<td><a href="https://rating.chgk.info/teams/4141">Чайники</a></td>
<td>Бостон</td>
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
<td><a href="https://rating.chgk.info/teams/39238">Побратимы</a></td>
<td>сборная</td>
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
<tr>
<td><a href="https://rating.chgk.info/teams/12840">Тай-брейк братской любви</a></td>
<td>сборная</td>
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
<tr>
<td><a href="https://rating.chgk.info/teams/42759">Хатуль Гитнакан</a></td>
<td>Чикаго</td>
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
<div class="country-tab-start" data-tab="players"></div>

<a id="players"></a>

<table>
<thead>
<tr><th rowspan="2">Игрок</th><th colspan="4" style="text-align:center">Все медали</th><th colspan="3" style="text-align:center">ЧГК</th><th colspan="3" style="text-align:center">БР</th><th colspan="3" style="text-align:center">ССИ</th></tr>
<tr><th>I</th><th>II</th><th>III</th><th>∑</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th><th>I</th><th>II</th><th>III</th></tr>
</thead>
<tbody>
<tr>
<td><a href="https://rating.chgk.info/player/2448">Вадим Барановский</a></td>
<td>14</td>
<td>11</td>
<td>5</td>
<td>30</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>0</td>
<td>5</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36537">Игорь Шпунгин</a></td>
<td>11</td>
<td>12</td>
<td>5</td>
<td>28</td>
<td>6</td>
<td>6</td>
<td>4</td>
<td>5</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23723">Григорий Остров</a></td>
<td>11</td>
<td>12</td>
<td>4</td>
<td>27</td>
<td>6</td>
<td>6</td>
<td>4</td>
<td>5</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4223">Константин Бриф</a></td>
<td>10</td>
<td>9</td>
<td>8</td>
<td>27</td>
<td>7</td>
<td>7</td>
<td>4</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12618">Римма Ионтель</a></td>
<td>11</td>
<td>9</td>
<td>4</td>
<td>24</td>
<td>6</td>
<td>5</td>
<td>4</td>
<td>5</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13811">Роман Кацыв</a></td>
<td>9</td>
<td>8</td>
<td>5</td>
<td>22</td>
<td>6</td>
<td>6</td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7935">Владимир Грамагин</a></td>
<td>7</td>
<td>10</td>
<td>4</td>
<td>21</td>
<td>3</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31400">Дмитрий Тейтельман</a></td>
<td>7</td>
<td>4</td>
<td>10</td>
<td>21</td>
<td>4</td>
<td>4</td>
<td>5</td>
<td>3</td>
<td>0</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15040">Леонид Койфман</a></td>
<td>8</td>
<td>4</td>
<td>6</td>
<td>18</td>
<td>4</td>
<td>3</td>
<td>4</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21001">Илья Миронов</a></td>
<td>5</td>
<td>4</td>
<td>9</td>
<td>18</td>
<td>3</td>
<td>3</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>5</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7476">Олег Гольденштейн</a></td>
<td>7</td>
<td>6</td>
<td>3</td>
<td>16</td>
<td>5</td>
<td>3</td>
<td>3</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/39658">Станислав Малышев</a></td>
<td>4</td>
<td>1</td>
<td>11</td>
<td>16</td>
<td>2</td>
<td>1</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30072">Александр Солодухин</a></td>
<td>6</td>
<td>5</td>
<td>4</td>
<td>15</td>
<td>4</td>
<td>4</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29950">Мария Соколова</a></td>
<td>5</td>
<td>3</td>
<td>7</td>
<td>15</td>
<td>3</td>
<td>3</td>
<td>4</td>
<td>2</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3242">Евгений Берман</a></td>
<td>6</td>
<td>4</td>
<td>4</td>
<td>14</td>
<td>4</td>
<td>4</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19025">Григорий Львович</a></td>
<td>6</td>
<td>5</td>
<td>2</td>
<td>13</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>3</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15890">Юрий Корчёмкин</a></td>
<td>5</td>
<td>5</td>
<td>3</td>
<td>13</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37245">Георгий Яковлев</a></td>
<td>3</td>
<td>0</td>
<td>10</td>
<td>13</td>
<td>2</td>
<td>0</td>
<td>5</td>
<td>1</td>
<td>0</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12656">Виктор Исаев</a></td>
<td>3</td>
<td>5</td>
<td>4</td>
<td>12</td>
<td>0</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11466">Евгений Затуловский</a></td>
<td>4</td>
<td>6</td>
<td>1</td>
<td>11</td>
<td>2</td>
<td>3</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30073">Вадим Солодухин</a></td>
<td>6</td>
<td>1</td>
<td>3</td>
<td>10</td>
<td>5</td>
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
<td><a href="https://rating.chgk.info/player/18277">Елена Лесных</a></td>
<td>4</td>
<td>4</td>
<td>2</td>
<td>10</td>
<td>3</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/8697">Мария Корчёмкина</a></td>
<td>4</td>
<td>3</td>
<td>3</td>
<td>10</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15155">Виталий Колмановский</a></td>
<td>3</td>
<td>3</td>
<td>4</td>
<td>10</td>
<td>2</td>
<td>3</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10951">Юлия Жоголева</a></td>
<td>3</td>
<td>0</td>
<td>7</td>
<td>10</td>
<td>2</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/69720">Максим Галкин</a></td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>9</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20072">Карен Марутян</a></td>
<td>3</td>
<td>2</td>
<td>3</td>
<td>8</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18583">Сергей Лобачёв</a></td>
<td>2</td>
<td>2</td>
<td>4</td>
<td>8</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15156">Леонид Колмановский</a></td>
<td>3</td>
<td>2</td>
<td>2</td>
<td>7</td>
<td>2</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6853">Мария Гендина</a></td>
<td>1</td>
<td>4</td>
<td>2</td>
<td>7</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10226">Матвей Егоров</a></td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>6</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25232">Ефим Подвойский</a></td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2033">Вардан Багирян</a></td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>6</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22046">Андрей Мягков</a></td>
<td>1</td>
<td>0</td>
<td>5</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18141">Олег Леденёв</a></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>5</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2942">Анна Белкина</a></td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28255">Ваган Сардарян</a></td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/217114">Николай Арчак</a></td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>4</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10936">Александр Житомирский</a></td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>4</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28103">Алексей Самсонов</a></td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/56704">Татьяна Веремеенко</a></td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5298">Борис Вейцман</a></td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td>1</td>
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
<td><a href="https://rating.chgk.info/player/4241">Дэль Бродская</a></td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1222">Рина Анно</a></td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20401">Юрий Мачкасов</a></td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>4</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/70429">Ольга Донич</a></td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27380">Полина Митриковская</a></td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>4</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4271">Леонид Брухис</a></td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>4</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/175797">Екатерина Александровская</a></td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28426">Иван Светлаков</a></td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>1</td>
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
<td><a href="https://rating.chgk.info/player/31416">Александр Тельнов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5056">Юлия Затуловская</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34916">Евгений Чёрный</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14004">Ольга Кижло-Чёрная</a></td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>3</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36442">Мария Шмилевич</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/1691">Ирина Асташкевич</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28212">Алексей Сапронов</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11726">Тимур Зильберштейн</a></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4861">Ирина Вайсертрейгер</a></td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20373">Марина Мацкевич</a></td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19776">Илья Мандель</a></td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15470">Алексей Кононенко</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31435">Вадим Тёмкин</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/5717">Денис Власов</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/144088">Олег Годовых</a></td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19699">Мамедшакир Мамедзаде</a></td>
<td>0</td>
<td>0</td>
<td>3</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10768">Дмитрий Жарков</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/224534">Дарья Костина</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29521">Дмитрий Слоущ</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/63177">Олег Родерик</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33620">Руслан Хаиткулов</a></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6832">Елена Гельзайд</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34909">Ирина Чернуха</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23116">Гани Нурмухаметов</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7467">Григорий Гольберг</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12170">Николай Иванов</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/19720">Турьян Рафаэли</a></td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11405">Владислав Зарайский</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27155">Андрей Романчев</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/20503">Инна Меерсон</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37157">Иван Юшин</a></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/15565">Александр Копылёв</a></td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32858">Роман Файнберг</a></td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17868">Илья Лапшин</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/25358">Олеся Покорная</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/124895">Сергей Серебряков</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22792">София Годовых</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21956">Тимур Мухаматулин</a></td>
<td>0</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12073">Александр Иванов</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/7759">Лев Горенштейн</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/110507">Виталий Киселёв</a></td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17045">Александр Кузьмин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/790">Андрей Алексеев-Попов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/61768">Борис Дзевенский</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/63179">Виталий Ермолин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3065">Вячеслав Бельков</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/65509">Георгий Энгельхардт</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/64721">Елена Наговицына</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35590">Роман Шапошников</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/288681">Юрий Барков</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/113202">Виктория Козьмина</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22935">Илья Новиков</a></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/29943">Ирина Соколова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/17851">Павел Лапицкий</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18162">Павел Лейдерман</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/33797">Павел Харитонов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/26855">Александр Ретах</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14915">Алексей Козин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/84796">Алексей Потехин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6913">Анна Герасимова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/39863">Виктория Кошурина</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/65516">Виталий Ражанский</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23845">Владимир Павлов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/21541">Дмитрий Мороз</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/36374">Дмитрий Шлеймович</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71477">Евгения Тейтельман</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/84797">Елена Вилешина</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37295">Илья Якубович</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/12467">Каринэ Чубарьян</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/84792">Леонид Литвак</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/32185">Леонид Трофимчук</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/6207">Марианна Выдревич</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/71710">Мария Якубович</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/65517">Нина Мироненко</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/13300">Сергей Каниськин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27062">Яна Рольник</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/2246">Александр Балаев</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31399">Анна Тейтельман</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/54855">Борис Бердников</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/34649">Денис Чебыкин</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/23095">Евгений Нудельман</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/47087">Евгения Финкельштейн</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22891">Ирина Новак</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/4863">Лев Вайсман</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/73545">Максим Пинкусович</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/58813">Наталья Бердникова</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/14549">Сергей Кныш</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/28988">Сергей Сиденко</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/35904">Сергей Шевченко</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/10284">Александра Езерская</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/52055">Бахтияр Нейман</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30197">Дмитрий Сорокурс</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/31831">Евгений Ткаченко</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/11983">Елена Зусманович</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/22468">Марк Неменман</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/305">Михаил Аврех</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/30306">Олег Спирт</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/37412">Ольга Ярославцева</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/184967">Пётр Мартынов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/3268">Роман Бершадский</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/237325">Александра Ломаева</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/87250">Анна Богусевич</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/138052">Анна Бондарь</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/284333">Владимир Пузырёв</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/18348">Галина Лившиц</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/27525">Кирилл Рыжов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><a href="https://rating.chgk.info/player/885">Станислав Алимпов</a></td>
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
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-chgk"></div>

<a id="game-chgk"></a><a id="chgk_contents" name="chgk_contents"></a>

- [XXVIII чемпионат США по спортивному ЧГК (2025)](#chgk_2025)
- [XXVII чемпионат США по спортивному ЧГК (2024)](#chgk_2024)
- [XXVI чемпионат США по спортивному ЧГК (2023)](#chgk_2023)
- [XXV чемпионат США по спортивному ЧГК (2020)](#chgk_2020)
- [XXIV чемпионат США по спортивному ЧГК (2019)](#chgk_2019)
- [XXIII чемпионат США по спортивному ЧГК (2018)](#chgk_2018)
- [XXII чемпионат США по спортивному ЧГК (2017)](#chgk_2017)
- [XXI чемпионат США по спортивному ЧГК (2016)](#chgk_2016)
- [XX чемпионат США по спортивному ЧГК (2015)](#chgk_2015)
- [XIX чемпионат США по спортивному ЧГК (2014)](#chgk_2014)
- [XVIII чемпионат США по спортивному ЧГК (2013)](#chgk_2013)
- [XVII чемпионат США по спортивному ЧГК (2012)](#chgk_2012)
- [XVI чемпионат США по спортивному ЧГК (2011)](#chgk_2011)
- [XV чемпионат США по спортивному ЧГК (2010)](#chgk_2010)
- [XIV чемпионат США по спортивному ЧГК (2009)](#chgk_2009)
- [XIII чемпионат США по спортивному ЧГК (2008)](#chgk_2008)
- [XII чемпионат США по спортивному ЧГК (2007)](#chgk_2007)
- [XI чемпионат США по спортивному ЧГК (2006)](#chgk_2006)
- [X чемпионат США по спортивному ЧГК (2005)](#chgk_2005)
- [IX чемпионат США по спортивному ЧГК (2004)](#chgk_2004)
- [VIII чемпионат США по спортивному ЧГК (2003)](#chgk_2003)
- [VII чемпионат США по спортивному ЧГК (2002)](#chgk_2002)
- [VI чемпионат США по спортивному ЧГК (2000)](#chgk_2000)
- [V чемпионат США по спортивному ЧГК (1999)](#chgk_1999)
- [IV чемпионат США по спортивному ЧГК (1998)](#chgk_1998)
- [III чемпионат США по спортивному ЧГК (1997)](#chgk_1997)
- [II чемпионат США по спортивному ЧГК (1996)](#chgk_1996)


**XXVIII чемпионат США по спортивному «Что? Где? Когда?»** прошёл 16–17 ноября 2025 года в Чикаго. <a id="chgk_2025"></a>

Победитель: **[«Надо подкачаться» (сборная)](https://rating.chgk.info/teams/105990)**
- Дарья Костина
- Николай Арчак
- Екатерина Александровская
- Дмитрий Тейтельман
- Дмитрий Слоущ
- Евгений Затуловский

Второе место заняла команда [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто), третье — [«Весёлые монахи»](https://rating.chgk.info/teams/46750) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/12840), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/6679). Фотографии с турнира можно посмотреть по [этой ссылке](https://www.facebook.com/groups/931240483905423/posts/2634084223621032/?__cft__[0]=AZhAfIiMaHyfYBHiOssFokb9Fu0ad3PxbL6gNmPYO8x96Av2G6tmxqKqia8b1U1K_24qvKDYz6tOWL5HsGrs5uOnMjeG_HLH8CMF4dMaGUzunalz4TnKMET9ogZ2L8ZxbFNqttxhqWopxz-PHCk3Juh3UrbNBTGRi7TVbNIXOHnrSm-LECuxDJCk3O-Ot6cD&__tn__=%2CO%2CP-R). Больше информации о турнире — [на сайте чемпионата](https://vnm.chgk.info/2025/index.html), [в Facebook](https://www.facebook.com/groups/931240483905423/?multi_permalinks=2634084223621032&hoisted_section_header_type=recently_seen&__cft__[0]=AZU_44PMzl62RcPDUujTNPA7C0cMQxRoVUlGAVa00qHbe4UMVIIpgh5nVcKy4sJUFnBegWBGefJ65zQvXnGQbtYbxSYAUwtXx0Z8yv3bdcHn-Y1Ve7GZnVz7cVfpkgIlt2Un6hO611yb2dlX15V0S3zmjdCnCk5dW-bn6vGWlOP_d-Ift3HFbOCXruuIAqz7jqrdoVyFKuKvddQiJYzWRhtf&__tn__=%2CO%2CP-R) и [здесь](https://t.me/chgknews/1309).

*[К оглавлению](#chgk_contents)*

---

**XXVII чемпионат США по спортивному «Что? Где? Когда?»** прошёл 16–17 ноября 2024 года в Лос-Анджелесе. <a id="chgk_2024"></a>

Победитель: **[«Кузинатра» (Сиэтл)](https://rating.chgk.info/teams/38917)**
- Максим Галкин
- Иван Светлаков
- Андрей Романчев
- Карен Марутян
- Юрий Корчёмкин
- Мария Корчёмкина

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк), третье — [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/11436), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/6523). Больше информации о турнире — [на сайте чемпионата](https://docs.google.com/document/d/e/2PACX-1vQfrrh1_kj3p-LWqmGt_jIqBkvmniAwGvAbP_dkaQ4h7qe9OJbVKd56h7lSzoYy4kXl5sHAvotVbBrc/pub), [в этом телеграм-канале](https://t.me/chgk_usa_2024) и [здесь](https://t.me/chgknews/987).

*[К оглавлению](#chgk_contents)*

---

**XXVI чемпионат США по спортивному «Что? Где? Когда?»** прошёл 11–12 ноября 2023 года в Филадельфии. <a id="chgk_2023"></a>

Победитель: **[«Инк» (Пало-Альто)](https://rating.chgk.info/teams/216)**
- Вадим Солодухин
- Александр Солодухин
- Сергей Лобачёв
- Елена Лесных
- Леонид Койфман
- Роман Кацыв
- Константин Бриф
- Евгений Берман

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк), третье — [«Кузинатра»](https://rating.chgk.info/teams/38917) (Сиэтл).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/9745), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/5743). Больше информации о турнире — [на сайте чемпионата](https://usachamp.chgk.info/2023/), [в Facebook](https://www.facebook.com/events/667024678205093/) и [здесь](https://t.me/chgknews/651).

*[К оглавлению](#chgk_contents)*

---

**XXV чемпионат США по спортивному «Что? Где? Когда?»** прошёл 7–8 марта 2020 года в Чикаго. <a id="chgk_2020"></a>

Победитель: **[«Инк» (Пало-Альто)](https://rating.chgk.info/teams/216)**
- Ирина Чернуха
- Вадим Солодухин
- Елена Лесных
- Роман Кацыв
- Константин Бриф
- Евгений Берман

Второе место заняла команда [«Заливная»](https://rating.chgk.info/teams/51796) (Пало-Альто), третье — [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/6220). Фотографии с турнира можно посмотреть по [этой ссылке](https://www.facebook.com/groups/931240483905423/posts/1073842092978594/?__cft__[0]=AZgQWOYlf4Xl2llytaBypzYyPBOoroQ88EuCW2BYIHbT-DcRoR_Th4xaYT6cdCRj5zvE2cotK56gg-gM68AmkAtm0E4cKXSMsb8kYAsJsHc2ZumEoZcuTcIyF_UNH1uidupDYWaYZ78DzRvUavwMcjTHgi1hA4O8cZyWRkSon0C_qC6zgxzNu_q2oB2iZvzISq_4cUy0BcXb10mudD1AsnuiKH00zhiI0-SDCx1fH09Ox4JETtWRvreKkKgYI9n9zIYb9lWiSwYDr3V3y1sHjJkqOR0OycvdnN29KGA0mDuRMJSORmhIHnfqOVupluGLqZ-XF7Abx0-vpqInkhWXB6rptg8AJQ8KjEs7y2N6&__tn__=%2CO%2CP-R). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20210620074138/http://vnm.chgk.info/2020/index.html), [в Facebook](https://www.facebook.com/events/649280039212508/permalink/693761568097688/) и [здесь](https://t.me/chgknews/9).

*[К оглавлению](#chgk_contents)*

---

**XXIV чемпионат США по спортивному «Что? Где? Когда?»** прошёл 23–25 марта 2019 года в Дублине. <a id="chgk_2019"></a>

Победитель: **[«АбВер: операция Туда, блин!» (Торонто)](https://rating.chgk.info/teams/69931)**
- Елена Наговицына
- Борис Дзевенский
- Евгений Чёрный
- Григорий Львович
- Ольга Кижло-Чёрная
- Вячеслав Бельков

Второе место заняла команда [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто), третье — [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/5490). Больше информации о турнире — [на сайте чемпионата](http://us2019.chgk.info/).

*[К оглавлению](#chgk_contents)*

---

**XXIII чемпионат США по спортивному «Что? Где? Когда?»** прошёл 24–25 марта 2018 года в Нью-Йорке. <a id="chgk_2018"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**
- Игорь Шпунгин
- Григорий Остров
- Римма Ионтель
- Владимир Грамагин
- Олег Гольденштейн
- Вадим Барановский

Второе место заняла команда [MW](https://rating.chgk.info/teams/55189) (Пало-Альто), третье — [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4846). Фотографии с турнира можно посмотреть по [этой ссылке](https://www.facebook.com/ZorroNYC/media_set?set=a.1585860228199514.1073742052.100003266565412&amp%3Btype=3&amp%3Buploaded=225&amp%3Bhc_location=ufi). Больше информации о турнире — [на сайте чемпионата](http://ny.chgk.info/2018/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/%D0%A7%D0%A1%D0%A8%D0%90-2018%20%D0%B2%20%D0%9D%D1%8C%D1%8E-%D0%94%D0%B6%D0%B5%D1%80%D1%81%D0%B8/) и [здесь](https://chgk-us.livejournal.com/205870.html).

*[К оглавлению](#chgk_contents)*

---

**XXII чемпионат США по спортивному «Что? Где? Когда?»** прошёл 8–9 апреля 2017 года в Чикаго. <a id="chgk_2017"></a>

Победитель: **[«Инк» (Пало-Альто)](https://rating.chgk.info/teams/216)**
- Александр Солодухин
- Елена Лесных
- Роман Кацыв
- Евгений Затуловский
- Юлия Затуловская
- Константин Бриф

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк), третье — [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/4221). Фотографии с турнира можно посмотреть по [этой ссылке](https://chgk-us.livejournal.com/187388.html). Больше информации о турнире — [на сайте чемпионата](https://vnm.chgk.info/2017/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/%D0%A7%D0%A1%D0%A8%D0%90-2017%20%D0%B2%20%D0%A7%D0%B8%D0%BA%D0%B0%D0%B3%D0%BE/) и [здесь](https://vnm.chgk.info/2017/results.html).

*[К оглавлению](#chgk_contents)*

---

**XXI чемпионат США по спортивному «Что? Где? Когда?»** прошёл 9–10 апреля 2016 года в Миннеаполисе. <a id="chgk_2016"></a>

Победитель: **[«Тормоза» (Пало-Альто)](https://rating.chgk.info/teams/446)**
- Станислав Малышев
- Георгий Яковлев
- Дмитрий Тейтельман
- Мария Соколова
- Илья Миронов
- Юлия Жоголева

Второе место заняла команда [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто), третье — [«Кузинатра»](https://rating.chgk.info/teams/38917) (Сиэтл).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3772). Больше информации о турнире — [на сайте чемпионата](http://mn2016.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2016%20в%20Миннеаполисе/), [здесь](https://chgk-us.livejournal.com/171806.html) и [в Летописи](http://letopis.chgk.info/201604Minneapolis.html).

*[К оглавлению](#chgk_contents)*

---

**XX чемпионат США по спортивному «Что? Где? Когда?»** прошёл 28–29 марта 2015 года в Дублине. <a id="chgk_2015"></a>

Победитель: **[«Тормоза» (Пало-Альто)](https://rating.chgk.info/teams/446)**
- Станислав Малышев
- Георгий Яковлев
- Дмитрий Тейтельман
- Мария Соколова
- Илья Миронов
- Юлия Жоголева

Второе место заняла команда [«Кузинатра»](https://rating.chgk.info/teams/38917) (Сиэтл), третье — [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/3226). Фотографии с турнира можно посмотреть по [этой ссылке](https://web.archive.org/web/20180510045538/http://us2015.chgk.info/memoirs). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20170713112611/http://us2015.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2015%20в%20Дублине/) и [в Летописи](http://letopis.chgk.info/201503Doublin.html).

*[К оглавлению](#chgk_contents)*

---

**XIX чемпионат США по спортивному «Что? Где? Когда?»** прошёл 20–21 марта 2014 года в Чикаго. <a id="chgk_2014"></a>

Победитель: **[«Инк» (Пало-Альто)](https://rating.chgk.info/teams/216)**
- Руслан Хаиткулов
- Вадим Солодухин
- Григорий Львович
- Леонид Койфман
- Роман Кацыв
- Константин Бриф

Второе место заняла команда [«Кузинатра»](https://rating.chgk.info/teams/38917) (Сиэтл), третье — [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2835). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20140727122850/http://vnm.chgk.info/2014/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2014%20в%20Чикаго/), [здесь](https://chgk-us.livejournal.com/151931.html) и [в Летописи](http://letopis.chgk.info/201403Chicago.html).

*[К оглавлению](#chgk_contents)*

---

**XVIII чемпионат США по спортивному «Что? Где? Когда?»** прошёл 19–20 апреля 2013 года в Сан-Франциско. <a id="chgk_2013"></a>

Победитель: **[Vademecum (Бостон)](https://rating.chgk.info/teams/7542)**
- Виталий Ермолин
- Юрий Мачкасов
- Дэль Бродская
- Анна Белкина
- Ирина Асташкевич

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк), третье — [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2279). Больше информации о турнире — [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2013%20в%20Дублине/) и [в Летописи](http://letopis.chgk.info/201304SanFranciscoBay.html).

*[К оглавлению](#chgk_contents)*

---

**XVII чемпионат США по спортивному «Что? Где? Когда?»** прошёл 19–21 апреля 2012 года в Денвере. <a id="chgk_2012"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**
- Олег Родерик
- Игорь Шпунгин
- Григорий Остров
- Римма Ионтель
- Олег Гольденштейн
- Вадим Барановский

Второе место заняла команда [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто), третье — [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/2059). Больше информации о турнире — [здесь](https://chgk-us.livejournal.com/123478.html) и [в Летописи](http://letopis.chgk.info/201204Denver.html).

*[К оглавлению](#chgk_contents)*

---

**XVI чемпионат США по спортивному «Что? Где? Когда?»** прошёл 28–30 апреля 2011 года в Чикаго. <a id="chgk_2011"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**
- Игорь Шпунгин
- Григорий Остров
- Римма Ионтель
- Владимир Грамагин
- Олег Гольденштейн
- Вадим Барановский

Второе место заняла команда [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто), третье — [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто). Чемпион определился при подсчёте рейтинга вопросов, поскольку перестрелка закончилась вничью.

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1753), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3768). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20160523115452/http://vnm.chgk.info/2011/), [в Живом Журнале](https://vnm.chgk.info/2011/index.html), [здесь](https://chgk-us.livejournal.com/108219.html) и [в Летописи](http://letopis.chgk.info/201104Chicago.html).

*[К оглавлению](#chgk_contents)*

---

**XV чемпионат США по спортивному «Что? Где? Когда?»** прошёл 23–24 апреля 2010 года в Бостоне. <a id="chgk_2010"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**
- Игорь Шпунгин
- Григорий Остров
- Римма Ионтель
- Владимир Грамагин
- Олег Гольденштейн
- Вадим Барановский

Второе место заняла команда [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто), третье — [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/633), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/3956). Больше информации о турнире — [в Живом Журнале](https://chgk-us.livejournal.com/95642.html), [здесь](https://chgk-us.livejournal.com/95642.html) и [в Летописи](http://letopis.chgk.info/201004Boston.html).

*[К оглавлению](#chgk_contents)*

---

**XIV чемпионат США по спортивному «Что? Где? Когда?»** прошёл 1–2 мая 2009 года в Нью-Йорке. <a id="chgk_2009"></a>

Победитель: **[«Инк» (Пало-Альто)](https://rating.chgk.info/teams/216)**
- Вадим Солодухин
- Александр Солодухин
- Олег Леденёв
- Леонид Койфман
- Роман Кацыв
- Константин Бриф
- Евгений Берман

Второе место заняла команда [Vademecum](https://rating.chgk.info/teams/7542) (Бостон), третье — [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/464), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4265). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20101126112755/http://nyopen2009.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2009%20в%20Нью-Йорке/), [здесь](https://chgk-us.livejournal.com/72833.html) и [в Летописи](http://letopis.chgk.info/200905NY.html).

*[К оглавлению](#chgk_contents)*

---

**XIII чемпионат США по спортивному «Что? Где? Когда?»** прошёл 28–29 марта 2008 года в Бостоне. <a id="chgk_2008"></a>

Победитель: **[«Инк» (Пало-Альто)](https://rating.chgk.info/teams/216)**
- Вадим Солодухин
- Александр Солодухин
- Олег Леденёв
- Леонид Койфман
- Роман Кацыв
- Константин Бриф
- Евгений Берман

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк), третье — [«Саша и медведи»](https://rating.chgk.info/teams/271) (Торонто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/326), вопросы турнира можно почитать [здесь](https://gotquestions.online/pack/4821). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20080515053659/http://chai3.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2008%20в%20Бостоне/) и [в Летописи](http://letopis.chgk.info/200803Boston.html).

*[К оглавлению](#chgk_contents)*

---

**XII чемпионат США по спортивному «Что? Где? Когда?»** прошёл 21–22 апреля 2007 года в Ливерморе. <a id="chgk_2007"></a>

Победитель: **[«Тормоза» (Пало-Альто)](https://rating.chgk.info/teams/446)**
- Александр Тельнов
- Дмитрий Тейтельман
- Мария Соколова
- Илья Миронов
- Леонид Колмановский
- Виталий Колмановский

Второе место заняла команда [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто), третье — [«Ботва»](https://rating.chgk.info/teams/2378) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/240).

*[К оглавлению](#chgk_contents)*

---

**XI чемпионат США по спортивному «Что? Где? Когда?»** прошёл 22 апреля 2006 года в Нью-Йорке. <a id="chgk_2006"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**
- Игорь Шпунгин
- Григорий Остров
- Римма Ионтель
- Александр Житомирский
- Елена Гельзайд
- Анна Белкина
- Рина Анно

Второе место заняла команда [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто), третье — [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/168). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20060626155509/http://nyopen2006.chgk.info/).

*[К оглавлению](#chgk_contents)*

---

**X чемпионат США по спортивному «Что? Где? Когда?»** прошёл 26 марта 2005 года в Лос-Анджелесе. <a id="chgk_2005"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**
- Григорий Остров
- Римма Ионтель
- Олег Гольденштейн
- Константин Бриф
- Игорь Шпунгин
- Александр Житомирский

Второе место заняла команда [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто), третье — [«Нонсенс»](https://rating.chgk.info/teams/138) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/77).

*[К оглавлению](#chgk_contents)*

---

**IX чемпионат США по спортивному «Что? Где? Когда?»** прошёл 10 апреля 2004 года в Вашингтоне. <a id="chgk_2004"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**

*Состав команды [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто), третье — [«Почти соседи»](https://rating.chgk.info/teams/799) (Нью-Йорк).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/40).

*[К оглавлению](#chgk_contents)*

---

**VIII чемпионат США по спортивному «Что? Где? Когда?»** прошёл 7 марта 2003 года в Пало-Альто. <a id="chgk_2003"></a>

Победитель: **[«Стоп-сигнал» (Пало-Альто)](https://rating.chgk.info/teams/231)**
- Юрий Барков
- Роман Шапошников
- Александр Кузьмин
- Леонид Колмановский
- Виталий Колмановский

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк), третье — [«Вечно живые»](https://rating.chgk.info/teams/449) (Пало-Альто).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1359).

*[К оглавлению](#chgk_contents)*

---

**VII чемпионат США по спортивному «Что? Где? Когда?»** прошёл 15–16 февраля 2002 года в Нью-Йорке. <a id="chgk_2002"></a>

Победитель: **[«Саша и медведи» (Торонто)](https://rating.chgk.info/teams/271)**

*Состав команды [«Саша и медведи»](https://rating.chgk.info/teams/271) (Торонто) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк), третье — [«Лямбда»](https://rating.chgk.info/teams/1181) (Нью-Йорк).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1234).

*[К оглавлению](#chgk_contents)*

---

**VI чемпионат США по спортивному «Что? Где? Когда?»** прошёл 8 апреля 2000 года в Нью-Йорке. <a id="chgk_2000"></a>

Победитель: **[«Лямбда» (Нью-Йорк)](https://rating.chgk.info/teams/1181)**

*Состав команды [«Лямбда»](https://rating.chgk.info/teams/1181) (Нью-Йорк) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Аппалачи»](https://rating.chgk.info/teams/37611) (Вашингтон), третье — [«Чайники»](https://rating.chgk.info/teams/4141) (Бостон).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1238).

*[К оглавлению](#chgk_contents)*

---

**V чемпионат США по спортивному «Что? Где? Когда?»** прошёл 27 ноября 1999 года в Лос-Анджелесе. <a id="chgk_1999"></a>

Победитель: **[«Спрайт» (Нью-Йорк)](https://rating.chgk.info/teams/29938)**

*Состав команды [«Спрайт»](https://rating.chgk.info/teams/29938) (Нью-Йорк) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто). Третье место разделили команды [«Нонсенс»](https://rating.chgk.info/teams/138) (Пало-Альто) и [«Палата №6»](https://rating.chgk.info/teams/29939) (сборная).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1036).

*[К оглавлению](#chgk_contents)*

---

**IV чемпионат США по спортивному «Что? Где? Когда?»** прошёл 31 января 1998 года в Нью-Йорке. <a id="chgk_1998"></a>

Победитель: **[«Аппалачи» (Вашингтон)](https://rating.chgk.info/teams/37611)**
- Георгий Энгельхардт
- Мария Шмилевич
- Владислав Зарайский
- Дмитрий Жарков
- Борис Вейцман
- Андрей Алексеев-Попов

Второе место заняла команда [«Вилладжеры»](https://rating.chgk.info/teams/4144) (Нью-Йорк). Третье место разделили команды [«Лямбда»](https://rating.chgk.info/teams/1181) (Нью-Йорк) и [«Матильда»](https://rating.chgk.info/teams/39746) (Нью-Йорк).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1913).

*[К оглавлению](#chgk_contents)*

---

**III чемпионат США по спортивному «Что? Где? Когда?»** прошёл 9 сентября 1997 года в Пало-Альто. <a id="chgk_1997"></a>

Победитель: **[«Аппалачи» (Вашингтон)](https://rating.chgk.info/teams/37611)**
- Дмитрий Жарков
 Больше информации о турнире — [в Летописи](http://letopis.chgk.info/199709USAIII.html).

*[К оглавлению](#chgk_contents)*

---

**II чемпионат США по спортивному «Что? Где? Когда?»** прошёл 22 февраля 1997 года в Нью-Йорке. <a id="chgk_1996"></a>

Победитель: **[«Аппалачи» (Вашингтон)](https://rating.chgk.info/teams/37611)**

*Состав команды [«Аппалачи»](https://rating.chgk.info/teams/37611) (Вашингтон) неизвестен. Если вы что-то о нём знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.*

Второе место заняла команда [«Чикаго»](https://rating.chgk.info/teams/32243) (Чикаго), третье — [«ВС+»](https://rating.chgk.info/teams/39739) (Нью-Йорк).

Полные результаты можно найти [на турнирном сайте](https://rating.chgk.info/tournament/1914).

*[К оглавлению](#chgk_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-brain"></div>

<a id="game-brain"></a><a id="brain_contents" name="brain_contents"></a>

- [XXV чемпионат США по БР (2025)](#brain_2025)
- [XXIV чемпионат США по БР (2024)](#brain_2024)
- [XXIII чемпионат США по БР (2023)](#brain_2023)
- [XXII чемпионат США по БР (2020)](#brain_2020)
- [XXI чемпионат США по БР (2019)](#brain_2019)
- [XX чемпионат США по БР (2018)](#brain_2018)
- [XIX чемпионат США по БР (2017)](#brain_2017)
- [XVIII чемпионат США по БР (2016)](#brain_2016)
- [XVII чемпионат США по БР (2015)](#brain_2015)
- [XVI чемпионат США по БР (2014)](#brain_2014)
- [XV чемпионат США по БР (2013)](#brain_2013)
- [XIV чемпионат США по БР (2012)](#brain_2012)
- [XIII чемпионат США по БР (2011)](#brain_2011)
- [XII чемпионат США по БР (2010)](#brain_2010)
- [XI чемпионат США по БР (2009)](#brain_2009)
- [X чемпионат США по БР (2008)](#brain_2008)


**XXV чемпионат США по брейн-рингу** прошёл 16–17 ноября 2025 года в Чикаго. <a id="brain_2025"></a>

Победитель: **[«Надо подкачаться» (сборная)](https://rating.chgk.info/teams/105990)**
- Дарья Костина
- Николай Арчак
- Екатерина Александровская
- Дмитрий Тейтельман
- Дмитрий Слоущ
- Евгений Затуловский

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк), третье — [«Тай-брейк братской любви»](https://rating.chgk.info/teams/12840) (сборная).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1lNp4S40pMs_Kvt_wBio99CmB1Z8L5giP4zJpGuxOANA/edit?gid=1323468111#gid=1323468111). Больше информации о турнире — [на сайте чемпионата](https://vnm.chgk.info/2025/index.html), [в Facebook](https://www.facebook.com/groups/931240483905423/?multi_permalinks=2634084223621032&hoisted_section_header_type=recently_seen&__cft__[0]=AZU_44PMzl62RcPDUujTNPA7C0cMQxRoVUlGAVa00qHbe4UMVIIpgh5nVcKy4sJUFnBegWBGefJ65zQvXnGQbtYbxSYAUwtXx0Z8yv3bdcHn-Y1Ve7GZnVz7cVfpkgIlt2Un6hO611yb2dlX15V0S3zmjdCnCk5dW-bn6vGWlOP_d-Ift3HFbOCXruuIAqz7jqrdoVyFKuKvddQiJYzWRhtf&__tn__=%2CO%2CP-R) и [здесь](https://t.me/chgknews/1309).

*[К оглавлению](#brain_contents)*

---

**XXIV чемпионат США по брейн-рингу** прошёл 16–17 ноября 2024 года в Лос-Анджелесе. <a id="brain_2024"></a>

Победитель: **[«Заливная» (Пало-Альто)](https://rating.chgk.info/teams/51796)**
- Евгений Затуловский
- Вардан Багирян
- Алексей Самсонов
- Татьяна Веремеенко
- Ирина Соколова
- Ирина Вайсертрейгер
- Елена Лесных
- Виктор Исаев

Второе место заняла команда [«НИИЧАВО»](https://rating.chgk.info/teams/79631) (Нью-Йорк), третье — [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто). Больше информации о турнире — [на сайте чемпионата](https://docs.google.com/document/d/e/2PACX-1vQfrrh1_kj3p-LWqmGt_jIqBkvmniAwGvAbP_dkaQ4h7qe9OJbVKd56h7lSzoYy4kXl5sHAvotVbBrc/pub), [в этом телеграм-канале](https://t.me/chgk_usa_2024) и [здесь](https://t.me/chgknews/987).

*[К оглавлению](#brain_contents)*

---

**XXIII чемпионат США по брейн-рингу** прошёл 11–12 ноября 2023 года в Филадельфии. <a id="brain_2023"></a>

Победитель: **[«Кузинатра» (Сиэтл)](https://rating.chgk.info/teams/38917)**
- Юрий Корчёмкин
- Мария Корчёмкина
- Максим Галкин
- Виктор Исаев
- Карен Марутян
- Иван Светлаков

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк), третье — [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто). Больше информации о турнире — [на сайте чемпионата](https://usachamp.chgk.info/2023/), [в Facebook](https://www.facebook.com/events/667024678205093/) и [здесь](https://t.me/chgknews/651).

*[К оглавлению](#brain_contents)*

---

**XXII чемпионат США по брейн-рингу** прошёл 7–8 марта 2020 года в Чикаго. <a id="brain_2020"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**
- Игорь Шпунгин
- Григорий Остров
- Инна Меерсон
- Римма Ионтель
- Владимир Грамагин
- Вадим Барановский

Второе место заняла команда [«Заливная»](https://rating.chgk.info/teams/51796) (Пало-Альто), третье — [«Весёлые монахи»](https://rating.chgk.info/teams/46750) (Пало-Альто).

Полные результаты можно найти [на этой странице](https://www.facebook.com/events/649280039212508/?post_id=693757051431473&view=permalink&__cft__[0]=AZghowsoo3H1R94zTXK51zA5lvNbINqNf3GgT4wfIUOKGXvoUVviBEamsM_1iWNLBEweRyqOBR75fImNHFlAmk6cs_6FsXhPgqDJdQ&__tn__=%2CO%2CP-R). Фотографии с турнира можно посмотреть по [этой ссылке](https://www.facebook.com/groups/931240483905423/posts/1073842092978594/?__cft__[0]=AZgQWOYlf4Xl2llytaBypzYyPBOoroQ88EuCW2BYIHbT-DcRoR_Th4xaYT6cdCRj5zvE2cotK56gg-gM68AmkAtm0E4cKXSMsb8kYAsJsHc2ZumEoZcuTcIyF_UNH1uidupDYWaYZ78DzRvUavwMcjTHgi1hA4O8cZyWRkSon0C_qC6zgxzNu_q2oB2iZvzISq_4cUy0BcXb10mudD1AsnuiKH00zhiI0-SDCx1fH09Ox4JETtWRvreKkKgYI9n9zIYb9lWiSwYDr3V3y1sHjJkqOR0OycvdnN29KGA0mDuRMJSORmhIHnfqOVupluGLqZ-XF7Abx0-vpqInkhWXB6rptg8AJQ8KjEs7y2N6&__tn__=%2CO%2CP-R). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20210620074138/http://vnm.chgk.info/2020/index.html), [в Facebook](https://www.facebook.com/events/649280039212508/permalink/693761568097688/) и [здесь](https://t.me/chgknews/9).

*[К оглавлению](#brain_contents)*

---

**XXI чемпионат США по брейн-рингу** прошёл 23–25 марта 2019 года в Дублине. <a id="brain_2019"></a>

Победитель: **[«Выше плинтуса» (Чикаго)](https://rating.chgk.info/teams/28217)**
- Ваган Сардарян
- Турьян Рафаэли
- Павел Лапицкий
- Павел Лейдерман
- Виктория Козьмина
- Павел Харитонов

Второе место заняла команда [«Весёлые монахи»](https://rating.chgk.info/teams/46750) (Пало-Альто), третье — [«Заливная»](https://rating.chgk.info/teams/51796) (Пало-Альто).

Полные результаты можно найти [на этой странице](http://us2019.chgk.info/br_res). Больше информации о турнире — [на сайте чемпионата](http://us2019.chgk.info/).

*[К оглавлению](#brain_contents)*

---

**XX чемпионат США по брейн-рингу** прошёл 24–25 марта 2018 года в Нью-Йорке. <a id="brain_2018"></a>

Победитель: **[«Кузинатра» (Сиэтл)](https://rating.chgk.info/teams/38917)**
- Мария Корчёмкина
- Виктор Исаев
- Карен Марутян
- Юрий Корчёмкин
- Мария Гендина
- Максим Галкин

Второе место заняла команда [«Веретено»](https://rating.chgk.info/teams/1966) (Торонто), третье — [«Заливная»](https://rating.chgk.info/teams/51796) (Пало-Альто).

Полные результаты можно найти [на этой странице](https://chgk-us.livejournal.com/205870.html). Фотографии с турнира можно посмотреть по [этой ссылке](https://chgk-us.livejournal.com/187388.html). Больше информации о турнире — [на сайте чемпионата](https://vnm.chgk.info/2017/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/%D0%A7%D0%A1%D0%A8%D0%90-2017%20%D0%B2%20%D0%A7%D0%B8%D0%BA%D0%B0%D0%B3%D0%BE/) и [здесь](https://vnm.chgk.info/2017/results.html).

*[К оглавлению](#brain_contents)*

---

**XIX чемпионат США по брейн-рингу** прошёл 8–9 апреля 2017 года в Чикаго. <a id="brain_2017"></a>

Победитель: **[«Тормоза» (Пало-Альто)](https://rating.chgk.info/teams/446)**
- Станислав Малышев
- Георгий Яковлев
- Дмитрий Тейтельман
- Мария Соколова
- Илья Миронов
- Юлия Жоголева

Второе место заняла команда [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто), третье — [«Кузинатра»](https://rating.chgk.info/teams/38917) (Сиэтл).

Фотографии с турнира можно посмотреть по [этой ссылке](https://chgk-us.livejournal.com/187388.html). Больше информации о турнире — [на сайте чемпионата](https://vnm.chgk.info/2017/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/%D0%A7%D0%A1%D0%A8%D0%90-2017%20%D0%B2%20%D0%A7%D0%B8%D0%BA%D0%B0%D0%B3%D0%BE/) и [здесь](https://vnm.chgk.info/2017/results.html).

*[К оглавлению](#brain_contents)*

---

**XVIII чемпионат США по брейн-рингу** прошёл 9–10 апреля 2016 года в Миннеаполисе. <a id="brain_2016"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**
- Игорь Шпунгин
- Григорий Остров
- Римма Ионтель
- Владимир Грамагин
- Вадим Барановский
- Гани Нурмухаметов

Второе место заняла команда [«Веретено»](https://rating.chgk.info/teams/1966) (Торонто), третье — [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто). Больше информации о турнире — [на сайте чемпионата](http://mn2016.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2016%20в%20Миннеаполисе/), [здесь](https://chgk-us.livejournal.com/171806.html) и [в Летописи](http://letopis.chgk.info/201604Minneapolis.html).

*[К оглавлению](#brain_contents)*

---

**XVII чемпионат США по брейн-рингу** прошёл 28–29 марта 2015 года в Дублине. <a id="brain_2015"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**
- Игорь Шпунгин
- Григорий Остров
- Римма Ионтель
- Владимир Грамагин
- Олег Гольденштейн
- Вадим Барановский

Второе место заняла команда [«Дом»](https://rating.chgk.info/teams/1099) (Бостон), третье — [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто).

Фотографии с турнира можно посмотреть по [этой ссылке](https://web.archive.org/web/20180510045538/http://us2015.chgk.info/memoirs). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20170713112611/http://us2015.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2015%20в%20Дублине/) и [в Летописи](http://letopis.chgk.info/201503Doublin.html).

*[К оглавлению](#brain_contents)*

---

**XVI чемпионат США по брейн-рингу** прошёл 20–21 марта 2014 года в Чикаго. <a id="brain_2014"></a>

Победитель: **[«Инк» (Пало-Альто)](https://rating.chgk.info/teams/216)**
- Руслан Хаиткулов
- Вадим Солодухин
- Григорий Львович
- Леонид Койфман
- Роман Кацыв
- Константин Бриф

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк), третье — [«Хатуль Гитнакан»](https://rating.chgk.info/teams/42759) (Чикаго).

Полные результаты можно найти [на этой странице](https://chgk-us.livejournal.com/151931.html). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20140727122850/http://vnm.chgk.info/2014/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2014%20в%20Чикаго/), [здесь](https://chgk-us.livejournal.com/151931.html) и [в Летописи](http://letopis.chgk.info/201403Chicago.html).

*[К оглавлению](#brain_contents)*

---

**XV чемпионат США по брейн-рингу** прошёл 19–20 апреля 2013 года в Сан-Франциско. <a id="brain_2013"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**
- Игорь Шпунгин
- Григорий Остров
- Римма Ионтель
- Владимир Грамагин
- Григорий Гольберг
- Вадим Барановский

Второе место заняла команда [«Соседи сверху»](https://rating.chgk.info/teams/44622) (сборная). Больше информации о турнире — [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2013%20в%20Дублине/) и [в Летописи](http://letopis.chgk.info/201304SanFranciscoBay.html).

*[К оглавлению](#brain_contents)*

---

**XIV чемпионат США по брейн-рингу** прошёл 19–21 апреля 2012 года в Денвере. <a id="brain_2012"></a>

Победитель: **[«Суббота 13» (Нью-Йорк)](https://rating.chgk.info/teams/1733)**
- Олег Родерик
- Игорь Шпунгин
- Григорий Остров
- Римма Ионтель
- Олег Гольденштейн
- Вадим Барановский

Второе место заняла команда [«Кузинатра»](https://rating.chgk.info/teams/38917) (Сиэтл), третье — [«Инк»](https://rating.chgk.info/teams/216) (Пало-Альто). Больше информации о турнире — [здесь](https://chgk-us.livejournal.com/123478.html) и [в Летописи](http://letopis.chgk.info/201204Denver.html).

*[К оглавлению](#brain_contents)*

---

**XIII чемпионат США по брейн-рингу** прошёл 28–30 апреля 2011 года в Чикаго. <a id="brain_2011"></a>

Победитель: **[«Инк» (Пало-Альто)](https://rating.chgk.info/teams/216)**
- Александр Солодухин
- Леонид Койфман
- Роман Кацыв
- Матвей Егоров
- Константин Бриф
- Евгений Берман

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк). Третье место разделили команды [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто) и [«Побратимы»](https://rating.chgk.info/teams/39238) (сборная).

Полные результаты можно найти [на этой странице](https://chgk-us.livejournal.com/108219.html). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20160523115452/http://vnm.chgk.info/2011/), [в Живом Журнале](https://vnm.chgk.info/2011/index.html), [здесь](https://chgk-us.livejournal.com/108219.html) и [в Летописи](http://letopis.chgk.info/201104Chicago.html).

*[К оглавлению](#brain_contents)*

---

**XII чемпионат США по брейн-рингу** прошёл 23–24 апреля 2010 года в Бостоне. <a id="brain_2010"></a>

Победитель: **[«Вестимо» (Торонто)](https://rating.chgk.info/teams/365)**
- Ефим Подвойский
- Тимур Зильберштейн
- Алексей Сапронов
- Николай Иванов
- Дмитрий Пикулик

Второе место заняла команда [«Американская солянка»](https://rating.chgk.info/teams/28288) (сборная), третье — [«Тормоза»](https://rating.chgk.info/teams/446) (Пало-Альто).

Полные результаты можно найти [на этой странице](https://chgk-us.livejournal.com/95642.html). Больше информации о турнире — [в Живом Журнале](https://chgk-us.livejournal.com/95642.html), [здесь](https://chgk-us.livejournal.com/95642.html) и [в Летописи](http://letopis.chgk.info/201004Boston.html).

*[К оглавлению](#brain_contents)*

---

**XI чемпионат США по брейн-рингу** прошёл 1–2 мая 2009 года в Нью-Йорке. <a id="brain_2009"></a>

Победитель: **[«Тормоза» (Пало-Альто)](https://rating.chgk.info/teams/446)**
- Станислав Малышев
- Дмитрий Тейтельман
- Мария Соколова
- Илья Миронов
- Леонид Колмановский
- Виталий Колмановский

Второе место заняла команда [«Суббота 13»](https://rating.chgk.info/teams/1733) (Нью-Йорк), третье — [Vademecum](https://rating.chgk.info/teams/7542) (Бостон).

Полные результаты можно найти [на этой странице](https://chgk-us.livejournal.com/72833.html). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20101126112755/http://nyopen2009.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2009%20в%20Нью-Йорке/), [здесь](https://chgk-us.livejournal.com/72833.html) и [в Летописи](http://letopis.chgk.info/200905NY.html).

*[К оглавлению](#brain_contents)*

---

**X чемпионат США по брейн-рингу** прошёл 28–29 марта 2008 года в Бостоне. <a id="brain_2008"></a>

Победитель: **[«Инк» (Пало-Альто)](https://rating.chgk.info/teams/216)**
- Александр Солодухин
- Олег Леденёв
- Леонид Койфман
- Роман Кацыв
- Константин Бриф
- Евгений Берман

Второе место заняла команда [«Почти соседи»](https://rating.chgk.info/teams/799) (Нью-Йорк), третье — [«Гексаэдр»](https://rating.chgk.info/teams/7542) (Бостон). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20080515053659/http://chai3.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2008%20в%20Бостоне/) и [в Летописи](http://letopis.chgk.info/200803Boston.html).

*[К оглавлению](#brain_contents)*

---

<div class="country-tab-end"></div>
<div class="country-tab-start" data-tab="game-ssi"></div>

<a id="game-ssi"></a><a id="ssi_contents" name="ssi_contents"></a>

- [XXI чемпионат США по ССИ (2025)](#ssi_2025)
- [XX чемпионат США по ССИ (2024)](#ssi_2024)
- [XIX чемпионат США по ССИ (2023)](#ssi_2023)
- [XVIII чемпионат США по ССИ (2020)](#ssi_2020)
- [XVII чемпионат США по ССИ (2019)](#ssi_2019)
- [XVI чемпионат США по ССИ (2018)](#ssi_2018)
- [XV чемпионат США по ССИ (2017)](#ssi_2017)
- [XIV чемпионат США по ССИ (2016)](#ssi_2016)
- [XIII чемпионат США по ССИ (2015)](#ssi_2015)
- [XII чемпионат США по ССИ (2014)](#ssi_2014)
- [XI чемпионат США по ССИ (2013)](#ssi_2013)
- [X чемпионат США по ССИ (2012)](#ssi_2012)
- [IX чемпионат США по ССИ (2011)](#ssi_2011)
- [VIII чемпионат США по ССИ (2010)](#ssi_2010)
- [VII чемпионат США по ССИ (2009)](#ssi_2009)
- [VI чемпионат США по ССИ (2008)](#ssi_2008)


**XXI чемпионат США по спортивной «Своей игре»** прошёл 16–17 ноября 2025 года в Чикаго. <a id="ssi_2025"></a>

Победитель: **[Николай Арчак](https://rating.chgk.info/player/217114)**

Второе место занял [Сергей Лобачёв](https://rating.chgk.info/player/18583), третье — [Мамедшакир Мамедзаде](https://rating.chgk.info/player/19699).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1YiMPBa2CEPo7PLzdZXsYX8OqqxCr3_oIMc5UoWRHW6I/edit?gid=1622237669#gid=1622237669). Больше информации о турнире — [на сайте чемпионата](https://vnm.chgk.info/2025/index.html), [в Facebook](https://www.facebook.com/groups/931240483905423/?multi_permalinks=2634084223621032&hoisted_section_header_type=recently_seen&__cft__[0]=AZU_44PMzl62RcPDUujTNPA7C0cMQxRoVUlGAVa00qHbe4UMVIIpgh5nVcKy4sJUFnBegWBGefJ65zQvXnGQbtYbxSYAUwtXx0Z8yv3bdcHn-Y1Ve7GZnVz7cVfpkgIlt2Un6hO611yb2dlX15V0S3zmjdCnCk5dW-bn6vGWlOP_d-Ift3HFbOCXruuIAqz7jqrdoVyFKuKvddQiJYzWRhtf&__tn__=%2CO%2CP-R) и [здесь](https://t.me/chgknews/1309).

*[К оглавлению](#ssi_contents)*

---

**XX чемпионат США по спортивной «Своей игре»** прошёл 16–17 ноября 2024 года в Лос-Анджелесе. <a id="ssi_2024"></a>

Победитель: **[Вадим Барановский](https://rating.chgk.info/player/2448)**

Второе место занял [Илья Миронов](https://rating.chgk.info/player/21001), третье — [Сергей Лобачёв](https://rating.chgk.info/player/18583). Больше информации о турнире — [на сайте чемпионата](https://docs.google.com/document/d/e/2PACX-1vQfrrh1_kj3p-LWqmGt_jIqBkvmniAwGvAbP_dkaQ4h7qe9OJbVKd56h7lSzoYy4kXl5sHAvotVbBrc/pub), [в этом телеграм-канале](https://t.me/chgk_usa_2024) и [здесь](https://t.me/chgknews/987).

*[К оглавлению](#ssi_contents)*

---

**XIX чемпионат США по спортивной «Своей игре»** прошёл 11–12 ноября 2023 года в Филадельфии. <a id="ssi_2023"></a>

Победитель: **[Сергей Лобачёв](https://rating.chgk.info/player/18583)**

Второе место занял [Григорий Львович](https://rating.chgk.info/player/19025), третье — [Андрей Романчев](https://rating.chgk.info/player/27155).

Полные результаты можно найти [в этой гуглтаблице](https://docs.google.com/spreadsheets/d/1T53eGcity6ytZaQaX01tbY1Zq7gyDIszh0ZdhZSaW8Q/edit?fbclid=IwAR0N_SARiIZfBGWMSmNWpyqzGbbdsCdfZBxDpK3V7zUsuiTKojg42Qy2xOA#gid=0). Больше информации о турнире — [на сайте чемпионата](https://usachamp.chgk.info/2023/), [в Facebook](https://www.facebook.com/events/667024678205093/) и [здесь](https://t.me/chgknews/651).

*[К оглавлению](#ssi_contents)*

---

**XVIII чемпионат США по спортивной «Своей игре»** прошёл 7–8 марта 2020 года в Чикаго. <a id="ssi_2020"></a>

Победитель: **[Вадим Барановский](https://rating.chgk.info/player/2448)**

Второе место занял [Григорий Львович](https://rating.chgk.info/player/19025), третье — [Мамедшакир Мамедзаде](https://rating.chgk.info/player/19699).

Полные результаты можно найти [на этой странице](https://www.facebook.com/events/649280039212508/?post_id=693761568097688&view=permalink&__cft__[0]=AZhxYbxjJUuz9DVRgETWU7RyuuP_khM1OxHmgmXyZIdUT4DzWzFnrY4xq_sVnq2E02Sf9gOYJWOD26xE37KVIp6ZgwrjL31bA1w3rA&__tn__=%2CO%2CP-R). Фотографии с турнира можно посмотреть по [этой ссылке](https://www.facebook.com/groups/931240483905423/posts/1073842092978594/?__cft__[0]=AZgQWOYlf4Xl2llytaBypzYyPBOoroQ88EuCW2BYIHbT-DcRoR_Th4xaYT6cdCRj5zvE2cotK56gg-gM68AmkAtm0E4cKXSMsb8kYAsJsHc2ZumEoZcuTcIyF_UNH1uidupDYWaYZ78DzRvUavwMcjTHgi1hA4O8cZyWRkSon0C_qC6zgxzNu_q2oB2iZvzISq_4cUy0BcXb10mudD1AsnuiKH00zhiI0-SDCx1fH09Ox4JETtWRvreKkKgYI9n9zIYb9lWiSwYDr3V3y1sHjJkqOR0OycvdnN29KGA0mDuRMJSORmhIHnfqOVupluGLqZ-XF7Abx0-vpqInkhWXB6rptg8AJQ8KjEs7y2N6&__tn__=%2CO%2CP-R). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20210620074138/http://vnm.chgk.info/2020/index.html), [в Facebook](https://www.facebook.com/events/649280039212508/permalink/693761568097688/) и [здесь](https://t.me/chgknews/9).

*[К оглавлению](#ssi_contents)*

---

**XVII чемпионат США по спортивной «Своей игре»** прошёл 23–25 марта 2019 года в Дублине. <a id="ssi_2019"></a>

Победитель: **[Илья Новиков](https://rating.chgk.info/player/22935)**

Второе место занял [Евгений Затуловский](https://rating.chgk.info/player/11466), третье — [Тимур Мухаматулин](https://rating.chgk.info/player/21956).

Полные результаты можно найти [на этой странице](http://us2019.chgk.info/si_results). Больше информации о турнире — [на сайте чемпионата](http://us2019.chgk.info/).

*[К оглавлению](#ssi_contents)*

---

**XVI чемпионат США по спортивной «Своей игре»** прошёл 24–25 марта 2018 года в Нью-Йорке. <a id="ssi_2018"></a>

Победитель: **[Мария Корчёмкина](https://rating.chgk.info/player/8697)**

Второе место занял [Тимур Мухаматулин](https://rating.chgk.info/player/21956), третье — [Григорий Львович](https://rating.chgk.info/player/19025).

Полные результаты можно найти [на этой странице](https://chgk-us.livejournal.com/205870.html). Фотографии с турнира можно посмотреть по [этой ссылке](https://www.facebook.com/ZorroNYC/media_set?set=a.1585860228199514.1073742052.100003266565412&amp%3Btype=3&amp%3Buploaded=225&amp%3Bhc_location=ufi). Больше информации о турнире — [на сайте чемпионата](http://ny.chgk.info/2018/) и [в Живом Журнале](https://chgk-us.livejournal.com/tag/%D0%A7%D0%A1%D0%A8%D0%90-2018%20%D0%B2%20%D0%9D%D1%8C%D1%8E-%D0%94%D0%B6%D0%B5%D1%80%D1%81%D0%B8/).

*[К оглавлению](#ssi_contents)*

---

**XV чемпионат США по спортивной «Своей игре»** прошёл 8–9 апреля 2017 года в Чикаго. <a id="ssi_2017"></a>

Победитель: **[Вадим Барановский](https://rating.chgk.info/player/2448)**

Второе место занял [Юрий Корчёмкин](https://rating.chgk.info/player/15890), третье — [Григорий Львович](https://rating.chgk.info/player/19025).

*[К оглавлению](#ssi_contents)*

---

**XIV чемпионат США по спортивной «Своей игре»** прошёл 9–10 апреля 2016 года в Миннеаполисе. <a id="ssi_2016"></a>

Победитель: **[Григорий Львович](https://rating.chgk.info/player/19025)**

Второе место занял [Вадим Барановский](https://rating.chgk.info/player/2448), третье — [Георгий Яковлев](https://rating.chgk.info/player/37245). Больше информации о турнире — [на сайте чемпионата](http://mn2016.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2016%20в%20Миннеаполисе/), [здесь](https://chgk-us.livejournal.com/171806.html) и [в Летописи](http://letopis.chgk.info/201604Minneapolis.html).

*[К оглавлению](#ssi_contents)*

---

**XIII чемпионат США по спортивной «Своей игре»** прошёл 28–29 марта 2015 года в Дублине. <a id="ssi_2015"></a>

Победитель: **[Юрий Корчёмкин](https://rating.chgk.info/player/15890)**

Второе место занял [Виктор Исаев](https://rating.chgk.info/player/12656), третье — [Леонид Брухис](https://rating.chgk.info/player/4271).

Полные результаты можно найти [на этой странице](https://web.archive.org/web/20180510044146/http://us2015.chgk.info/si_results). Фотографии с турнира можно посмотреть по [этой ссылке](https://web.archive.org/web/20180510045538/http://us2015.chgk.info/memoirs). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20170713112611/http://us2015.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2015%20в%20Дублине/) и [в Летописи](http://letopis.chgk.info/201503Doublin.html).

*[К оглавлению](#ssi_contents)*

---

**XII чемпионат США по спортивной «Своей игре»** прошёл 20–21 марта 2014 года в Чикаго. <a id="ssi_2014"></a>

Победитель: **[Юрий Корчёмкин](https://rating.chgk.info/player/15890)**

Второе место занял [Игорь Шпунгин](https://rating.chgk.info/player/36537), третье — [Вадим Барановский](https://rating.chgk.info/player/2448).

Полные результаты можно найти [на этой странице](https://chgk-us.livejournal.com/151931.html). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20140727122850/http://vnm.chgk.info/2014/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2014%20в%20Чикаго/), [здесь](https://chgk-us.livejournal.com/151931.html) и [в Летописи](http://letopis.chgk.info/201403Chicago.html).

*[К оглавлению](#ssi_contents)*

---

**XI чемпионат США по спортивной «Своей игре»** прошёл 19–20 апреля 2013 года в Сан-Франциско. <a id="ssi_2013"></a>

Победитель: **[Вадим Барановский](https://rating.chgk.info/player/2448)**

Второе место занял [Юрий Корчёмкин](https://rating.chgk.info/player/15890).

*На этом турнире часть призёров неизвестна. Если вы что-то о них знаете, напишите, пожалуйста, на <chgknews.info@gmail.com>.* Больше информации о турнире — [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2013%20в%20Дублине/) и [в Летописи](http://letopis.chgk.info/201304SanFranciscoBay.html).

*[К оглавлению](#ssi_contents)*

---

**X чемпионат США по спортивной «Своей игре»** прошёл 19–21 апреля 2012 года в Денвере. <a id="ssi_2012"></a>

Победитель: **[Андрей Мягков](https://rating.chgk.info/player/22046)**

Второе место занял [Матвей Егоров](https://rating.chgk.info/player/10226), третье — [Леонид Брухис](https://rating.chgk.info/player/4271). Больше информации о турнире — [здесь](https://chgk-us.livejournal.com/123478.html) и [в Летописи](http://letopis.chgk.info/201204Denver.html).

*[К оглавлению](#ssi_contents)*

---

**IX чемпионат США по спортивной «Своей игре»** прошёл 28–30 апреля 2011 года в Чикаго. <a id="ssi_2011"></a>

Победитель: **[Леонид Койфман](https://rating.chgk.info/player/15040)**

Второе место занял [Григорий Остров](https://rating.chgk.info/player/23723), третье — [Игорь Шпунгин](https://rating.chgk.info/player/36537).

Полные результаты можно найти [на этой странице](https://chgk-us.livejournal.com/108219.html). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20160523115452/http://vnm.chgk.info/2011/), [в Живом Журнале](https://vnm.chgk.info/2011/index.html), [здесь](https://chgk-us.livejournal.com/108219.html) и [в Летописи](http://letopis.chgk.info/201104Chicago.html).

*[К оглавлению](#ssi_contents)*

---

**VIII чемпионат США по спортивной «Своей игре»** прошёл 23–24 апреля 2010 года в Бостоне. <a id="ssi_2010"></a>

Победитель: **[Григорий Львович](https://rating.chgk.info/player/19025)**

Второе место занял [Константин Бриф](https://rating.chgk.info/player/4223), третье — [Олег Леденёв](https://rating.chgk.info/player/18141).

Полные результаты можно найти [на этой странице](https://chgk-us.livejournal.com/95642.html). Больше информации о турнире — [в Живом Журнале](https://chgk-us.livejournal.com/95642.html), [здесь](https://chgk-us.livejournal.com/95642.html) и [в Летописи](http://letopis.chgk.info/201004Boston.html).

*[К оглавлению](#ssi_contents)*

---

**VII чемпионат США по спортивной «Своей игре»** прошёл 1–2 мая 2009 года в Нью-Йорке. <a id="ssi_2009"></a>

Победитель: **[Григорий Львович](https://rating.chgk.info/player/19025)**

Второе место занял [Леонид Койфман](https://rating.chgk.info/player/15040), третье — [Константин Бриф](https://rating.chgk.info/player/4223).

Полные результаты можно найти [на этой странице](https://chgk-us.livejournal.com/72833.html). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20101126112755/http://nyopen2009.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2009%20в%20Нью-Йорке/), [здесь](https://chgk-us.livejournal.com/72833.html) и [в Летописи](http://letopis.chgk.info/200905NY.html).

*[К оглавлению](#ssi_contents)*

---

**VI чемпионат США по спортивной «Своей игре»** прошёл 28–29 марта 2008 года в Бостоне. <a id="ssi_2008"></a>

Победитель: **[Вадим Барановский](https://rating.chgk.info/player/2448)**

Второе место занял [Роман Кацыв](https://rating.chgk.info/player/13811), третье — [Константин Бриф](https://rating.chgk.info/player/4223). Больше информации о турнире — [на сайте чемпионата](https://web.archive.org/web/20080515053659/http://chai3.chgk.info/), [в Живом Журнале](https://chgk-us.livejournal.com/tag/ЧСША-2008%20в%20Бостоне/) и [в Летописи](http://letopis.chgk.info/200803Boston.html).

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
<tr><td>2013</td><td>XV чемпионат США по БР</td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>2013</td><td>XI чемпионат США по ССИ</td><td>неизвестен обладатель третьего места.</td></tr>
<tr><td>2005</td><td><a href="https://rating.chgk.info/tournament/77">X чемпионат США по ЧГК</a></td><td>неизвестны составы победителя и обладателей третьего места.</td></tr>
<tr><td>2004</td><td><a href="https://rating.chgk.info/tournament/40">IX чемпионат США по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2002</td><td><a href="https://rating.chgk.info/tournament/1234">VII чемпионат США по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>2000</td><td><a href="https://rating.chgk.info/tournament/1238">VI чемпионат США по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>1999</td><td><a href="https://rating.chgk.info/tournament/1036">V чемпионат США по ЧГК</a></td><td>неизвестны составы победителя и обладателей третьего места.</td></tr>
<tr><td>1998</td><td><a href="https://rating.chgk.info/tournament/1913">IV чемпионат США по ЧГК</a></td><td>неизвестен состав обладателей третьего места.</td></tr>
<tr><td>1997</td><td>III чемпионат США по ЧГК</td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
<tr><td>1996</td><td><a href="https://rating.chgk.info/tournament/1914">II чемпионат США по ЧГК</a></td><td>неизвестны составы победителя и обладателей второго и третьего мест.</td></tr>
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
<tr><td>XXIV чемпионат США по БР</td><td>2024</td><td><a href="https://t.me/postmortemchannel/1954">пост в телеграм-канале Postmortem</a> (состав победителей брейна)</td></tr>
<tr><td>XXV чемпионат США по ЧГК</td><td>2020</td><td><a href="https://www.facebook.com/events/649280039212508/?post_id=693751721432006&amp;view=permalink&amp;__cft__[0]=AZixKduj8Snj1Dq0SltqxshM36zCwoEk6wmkt6Ns1U419511jXF-BIcd1f18mWHndwoV8xyIKbHcAwm5haoFefvJ679Hg7KNcb6AHQ&amp;__tn__=%2CO%2CP-R">пост в мероприятии чемпионата в Фейсбуке</a> (результаты перестрелки в ЧГК)</td></tr>
<tr><td>XVIII чемпионат США по ССИ</td><td>2020</td><td><a href="https://www.facebook.com/events/649280039212508/?post_id=693761568097688&amp;view=permalink&amp;__cft__[0]=AZhxYbxjJUuz9DVRgETWU7RyuuP_khM1OxHmgmXyZIdUT4DzWzFnrY4xq_sVnq2E02Sf9gOYJWOD26xE37KVIp6ZgwrjL31bA1w3rA&amp;__tn__=%2CO%2CP-R">пост в мероприятии чемпионата в Фейсбуке</a> (призёры ССИ)</td></tr>
<tr><td>XVI чемпионат США по ССИ</td><td>2018</td><td><a href="https://chgk-us.livejournal.com/204519.html">пост в ЖЖ chgk_us</a> (участники свояка)</td></tr>
<tr><td>XI чемпионат США по ССИ</td><td>2013</td><td><a href="https://undamaris.livejournal.com/389196.html">пост в ЖЖ Марии Корчёмкиной</a> (серебряный призёр свояка), <a href="https://vgramagin.livejournal.com/302674.html">пост в ЖЖ Владимира Грамагина</a> (победитель свояка)</td></tr>
</tbody>
</table>

<div class="country-tab-end"></div>
