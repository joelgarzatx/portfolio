
var counter = 0;
var boxes = [];

window.onload = init;

function Box(id, name, color, x, y) {
  this.id = id;
  this.name = name;
  this.color = color;
  this.x = x;
  this.y = y;

}

  
function clear() {

var theScene = document.getElementById("scene");
theScene.innerHTML = "";
counter = 0;
boxes = [];

}
  
function init() {

   var generate_btn = document.getElementById("generateButton");
   generate_btn.onclick = generate;
   var clear_btn = document.getElementById("clearButton");
   clear_btn.onclick = clear;
}

function display(e) {
    var e = window.event || e;
    var targ = e.target || e.srcElement;
    
    var box_id = targ.getAttribute('id');
       
    var s = 'You clicked on a box with id ' + boxes[box_id].id + 
            ', named ' + boxes[box_id].name + 
            ', whose color is ' + boxes[box_id].color + 
            ', at position ' + boxes[box_id].x + 
            ', ' + boxes[box_id].y;
    alert(s);
};

function generate() {
//  window.alert('generate function');
  
  var theForm = document.getElementById("data"); 
  var nameInput = document.getElementById('name');
  var name = nameInput.value;
  
  var colorSelect = document.getElementById('color');
  var colorOption = colorSelect.options[colorSelect.selectedIndex];
  var color = colorOption.value;
  
  var amount = 0;
  var amountArray = document.getElementsByName('amount');
  for (var i=0; i < amountArray.length; i++) {
    if (amountArray[i].checked) {
       amount = amountArray[i].value;
       break;
    }
  } 
  if ( name == null || name == "" ) {
    alert('Please enter a name for the boxes!');
    return;
  } else if ( amount == 0 ) {
    alert('Please choose a number of boxes!');
    return;
  } else {
  
  
  for (var j=0; j<amount; j++) {
      
    var box_div = document.createElement("div");
    box_div.setAttribute("class","box");
    box_div.setAttribute("id", counter);
    box_div.style.backgroundColor = color;
    box_div.innerHTML = name;
    box_div.onClick = addEventListener('click',display,false);
    var theScene = document.getElementById("scene");
    var x = Math.floor(Math.random() * (theScene.offsetWidth-101));
    var y = Math.floor(Math.random() * (theScene.offsetHeight-101));
    
    box_div.style.left = x +'px';
    box_div.style.top = y + 'px';
    
    var box = new Box(counter, name, color, x, y);
    boxes.push(box);
    theScene.appendChild(box_div);
     
    counter += 1;
  }
  theForm.reset();
  }
}



