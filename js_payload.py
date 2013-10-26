payload = """var targetNodes = [];


var buttonHolder = document.createElement('div');
buttonHolder.setAttribute('data-grabthis', "scaffolding");

var readyButton = document.createElement('button');

readyButton.innerHTML = "get me my data yo";
readyButton.setAttribute('data-grabthis', "scaffolding");
readyButton.action = "alert('hello world');"


var addNodeToScraper = function(targetNode) {
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
	var targetNode = click.target;

	addNodeToScraper(targetNode);

	// blur out of the element when user hits "enter"
	targetNode.addEventListener("keydown", function (key) {
		// "enter" key registers as 13
		if (key.which == 13) {

			var targetLabelPattern = /\{\{(.*)\}\}/
			var targetLabelText = targetNode.textContent.match(targetLabelPattern)[1];

			targetNode.setAttribute('data-grabthis', targetLabelText);		
			targetNode.blur();

		}
	})

})"""