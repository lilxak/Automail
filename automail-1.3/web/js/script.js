var listEps;
var selectedEps = "";
function print_num(n) {
    if(n==1){
        $('#goodInfos').html('<h3>Sent successfully</h3>');
        $('#goodInfos').css('display','block');
        $('#myModal').modal('show');
    }
    else{
        $('#badInfos').html('<h3>Error</h3>');
        $('#badInfos').css('display','block');
        $('#myModal').modal('show');
    }
}
function sendMail(){
    let myLink = document.querySelector("#myLink").value;
    let mySubject = document.querySelector("#mySubject").value;
    let myContent = document.querySelector("#myContent").value;
    if(myLink=='' || myContent=='' || mySubject=='')
    {
        //alert('There are empty fields !')
        $('#badInfos').html('<h3>There are empty fields !</h3>')
        $('#badInfos').css('display','block');
        $('#myModal').modal('show');
    }
    else{
        eel.sendMailPy(myLink,mySubject,myContent)(print_num);
    }
}

function setLink(n){
    document.querySelector("#myLink").value = n;
}
function getLink(){
    eel.fileDialog()(setLink);
}



var myheight = 270;
$(document).ready(function() {
    $('#myContent').summernote({
        height:myheight,
        toolbar: [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    });
});

var myheightExpa = 250;
$(document).ready(function() {
    $('#myContentExpa').summernote({
        height:myheightExpa,
        toolbar: [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link']],
            ['view', ['fullscreen', 'codeview', 'help']],
        ],
    });
});

function fromSheet(){
    $('#home').css('display','none');
    $('#sheet').css('display','block'); 
}
function sheetToHome(){
    $('#sheet').css('display','none');
    $('#home').css('display','block'); 
}

function expaToHome(){
    $('#expa').css('display','none');
    $('#home').css('display','block'); 
}

function fromExpa(){
    $('#home').css('display','none');
    $('#expa').css('display','block'); 
}
function getEps(){
    let token = document.querySelector("#myToken").value;
    if(token=='')
    {
        $('#badInfos').html('<h3>Put your token please !</h3>')
        $('#badInfos').css('display','block');
        $('#myModal').modal('show');
    }
    else{
        eel.getEpsFromPython(token)(selectEps);
    }
}

function selectEps(eps){
    listEps = eps.split(';')
    $('#setEps').html('<div id=\'myEps\' style="height: 300px; overflow: auto;padding:30px"></div>');
    var i;
    for (i = 0 ;i <listEps.length;i++){
        text = "<div class=\"form-check\">\
            <input class=\"form-check-input \" type=\"checkbox\"  id=\"epID"+i+"\">\
            <label class=\"form-check-label col\" style=\"padding-left:20px;color: #fff;font-size: 2em;width:60%\"id=\"epName"+i+" for=\"epID"+i+"\">\
            "+listEps[i]+"\
            </label>\
            <input class=\"form-check-input col\" type=\"datetime-local\" style=\"width:35%\"  id=\"epDate"+i+"\">\
        </div>"
        $('#myEps').append(text);
    }
    $('#expa').css('display','none');
    $('#selectEps').css('display','block');
}

function selectToExpa(){
    $('#selectEps').css('display','none');
    $('#expa').css('display','block');
}

function getSelectedEps(){
    selectedEps = "";
    var children = $("#myEps").children().length;
    var i;
    for (i =0 ;i<children;i++){
        var id = "#epID".concat(i);
        if($(id).is(":checked")){
            var dateId = "epDate".concat(i);
            var date = document.getElementById(dateId).value;
            if(selectedEps ==""){
                selectedEps = selectedEps.concat(listEps[i]+"#"+date);
            }
            else{
                selectedEps = selectedEps.concat(";"+listEps[i]+"#"+date);
            }
        }     
    }
    if(selectedEps ==""){
        $('#badInfos').html('<h3>Select Eps pleas</h3>');
        $('#badInfos').css('display','block');
        $('#myModal').modal('show');
    }
    else{
        $('#selectEps').css('display','none');
        $('#templateEmail').css('display','block');
    }
}

function templateToSelect(){
    $('#templateEmail').css('display','none');
    $('#selectEps').css('display','block');
}

function sendFromExpa(){
    let mySubject = document.querySelector("#mySubjectExpa").value;
    let myContent = document.querySelector("#myContentExpa").value;
    if(myContent=='' || mySubject=='')
    {
        $('#badInfos').html('<h3>There are empty fields !</h3>')
        $('#badInfos').css('display','block');
        $('#myModal').modal('show');
    }
    else{
        eel.sendMailExpa(selectedEps,mySubject,myContent)(print_num);
    }
}

$('#badInfos').css('display','none');
$('#goodInfos').css('display','none');