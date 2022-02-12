var nextPosition = "left_block";

const URL = 'http://127.0.0.1:8000/'


function createInlineBlock(element) {
    var item, out;
    out = document.getElementById('out')

    if (nextPosition == 'left_block') { item = '<div class "wrapper"><div class="' + nextPosition + '"><div class="container-image">' }
    else { item = '<div class="' + nextPosition + '"><div class="container-image">' }

    item += '<img src="' + element.fields.image_url + '" alt="image" >';
    
    item += '<div class="item-text">';
    item += '<table>'
    item += '<tr><th>Manufacturer:</th><td>' + element.fields.manufacturer + '</td></tr>';
    item += '<tr><th>model:</th><td>' + element.fields.model + '</td></tr>';
    item += '<tr><th>category:</th><td>' + element.fields.category + '</td></tr>';
    item += '<tr><th>price:</th><td>' + element.fields.price + '</td></tr>';
    item += '<tr><th>Code of product:</th><td>' + element.fields.code_of_product + '</td></tr>';
    item += '<tr><th>Size of display:</th><td>' + element.fields.display + '</td></tr>';
    item += '<tr><th>Number cores:</th><td>' + element.fields.number_cores + '</td></tr>';
    item += '<tr><th>Processor:</th><td>' + element.fields.processor + '</td></tr>';
    item += '<tr><th>Producing country:</th><td>' + element.fields.producing_country + '</td></tr>';
    item += '<tr><th>Weight:</th><td>' + element.fields.weight + '</td></tr>';
    item += '<tr><th>Description:</th><td>' + element.fields.description + '</td></tr>';
    item += '<tr><th>Dimensions:</th><td>' + element.fields.dimensions + '</td></tr>';
    item += '<tr><th>Complete set:</th><td>' + element.fields.complete_set + '</td></tr>';
    item += '<a href="' + URL + element.pk + '/delete_phone' + '"><button class="btn btn-warning">delete</button></a>'
    item += '</table></div></div></div>';

    if (nextPosition == 'left_block') { nextPosition = 'right_block'; }
    else { nextPosition = 'left_block'; }
    out.outerHTML += item;
}


function parseObjects() {
    var objectList;
    objectList = JSON.parse(document.getElementById('objectList').value)

    Array.from(objectList).forEach(element => createInlineBlock(element));
    
    if (nextPosition == 'left_block') { out.outerHTML += '<div class="wrapper">'; }
}


parseObjects();