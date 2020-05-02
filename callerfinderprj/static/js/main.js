document.onreadystatechange = function () {
  var state = document.readyState
  if (state == 'interactive') {
    console.log('Loading');
  } else if (state == 'complete') {
      setTimeout(function(){
         document.getElementById('load').style.visibility="hidden";
      },1000);
  }
}