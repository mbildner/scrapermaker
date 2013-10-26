payload = """var targetNodes = [];


var buttonHolder = document.createElement('div');
buttonHolder.setAttribute('data-grabthis', "scaffolding");

var readyButton = document.createElement('button');

readyButton.innerHTML = "get me my data yo";
readyButton.setAttribute('data-grabthis', "scaffolding");
readyButton.action = "alert('hello world');"


buttonHolder.appendChild(readyButton);


document.body.insertBefore(buttonHolder, document.body.firstChild);



var register = function(targetNode) {
	var registered = targetNode.getAttribute('data-grabthis');

	if (!registered) {
		targetNode.setAttribute('contenteditable', true);
		var text = targetNode.textContent;
		var newText = "***GRAB THIS: {{your title here}}*** " + text;
		targetNode.textContent = newText;
		targetNode.setAttribute('data-grabthis', true);
		// targetNode.className += " GRABTHIS";
	} else {
		console.log(targetNode.className);
	}
}

document.addEventListener('click', function(click) {
	register(click.target);
})"""