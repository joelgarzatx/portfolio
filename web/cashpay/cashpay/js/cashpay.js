var counter = 0;
var payNodes = [];
var currencyAmounts = [100,50,20,10,5,1,0.25,0.10,0.05,0.01]
var currencyNames = ["Hundred", "Fifty", "Twenty", "Ten", "Five", "One", "Quarter", "Dime", "Nickel", "Penny"]


window.onload = init;

function PayNode(amount, note) {
	this.amount = amount;
	this.note = note;
	this.currency = [0,0,0,0,0,0,0,0,0,0]
}

function calculateAmounts(payNode) {
	amount = payNode.amount;
	var quantity;
	for(var i=0; i<10; i++) {
		quantity = Math.floor( amount / currencyAmounts[i] );
		amount = amount - ( quantity * currencyAmounts[i] );
		payNode.currency[i] = quantity;
	}
  return;
}

function init() {
    var generate_btn = document.getElementById("generateButton");
    generate_btn.onclick = generate;
    var clear_btn = document.getElementById("clearButton");
    clear_btn.onclick = clear;
}

function generate(){

	var theForm = document.getElementById("data");

	var amountInput = document.getElementById("amount");
	var amount = amountInput.value;

	var noteInput = document.getElementById("note");
	var note = noteInput.value;

	if ( amount == null || amount == "" || isNaN(parseFloat(amount))) {
		alert('Please enter a valid payment amount');
		return;
	}
    amount = parseFloat(amount);
    
    // create a payNode object and calculate the breakdown
    var payNode = new PayNode(amount, note);
    calculateAmounts(payNode);
    payNodes.push(payNode);

    // maintain list of items entered
    var pay_li = document.createElement("li");
    pay_li.setAttribute("class","list-group-item");
    pay_li.setAttribute("id", counter);
    pay_li.textContent = "$" + amount + ", " + note;   
    var theList = document.getElementById("list");
    theList.appendChild(pay_li);

    // update the totals in the currency table
    var currencyTotals = [0,0,0,0,0,0,0,0,0,0];
    for (var i=0; i<payNodes.length; i++) {
        for ( var j=0; j<10; j++) {
        	currencyTotals[j] += payNodes[i].currency[j];
        }
    }
    
    var td_div;
    for (var j=0; j<10; j++) {
    	td_div = document.getElementById(currencyNames[j]);
    	td_div.textContent = currencyTotals[j];
    }

    counter += 1;

}

function clear() {
	var theList = document.getElementById("list");
	theList.innerHTML = "";

    var td_div;
    for (var j=0; j<10; j++) {
    	td_div = document.getElementById(currencyNames[j]);
    	td_div.textContent = "0";
    }

	return;
}