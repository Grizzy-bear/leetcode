{/* <script type="text/javascript">  */}
//要想滑动不停  scroll_begin的内容宽度必须大于scroll_div的宽度
function ScrollImgLeft(){ 
    var speed=50; 
    var scroll_begin = document.getElementById("scroll_begin"); 
    var scroll_end = document.getElementById("scroll_end"); 
    var scroll_div = document.getElementById("scroll_div"); 
    scroll_end.innerHTML=scroll_begin.innerHTML; 
    function Marquee(){ 
          //offsetWidth  width + border + padding
         //scrollleft 滑动条起点向右滑动的距离 当一个div显示完后 迅速重置滑动条的起点为最左端 重新显示div内容
        if(scroll_end.offsetWidth-scroll_div.scrollLeft<=0) 
            scroll_div.scrollLeft-=scroll_begin.offsetWidth; 
        else 
            scroll_div.scrollLeft++; 
    } 
    var MyMar=setInterval(Marquee,speed); 
    scroll_div.onmouseover=function() {clearInterval(MyMar);} 
    scroll_div.onmouseout=function() {MyMar=setInterval(Marquee,speed);} 
} 
// </script> 