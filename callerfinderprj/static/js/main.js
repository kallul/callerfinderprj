document.onreadystatechange = function () {
  var state = document.readyState
  if (state == 'interactive') {
    console.log('Loading');
  } else if (state == 'complete') {
      setTimeout(function(){
		  var t = document.getElementById('load');
         if (t) t.style.display='none';		 
      },1000);
  }
}
