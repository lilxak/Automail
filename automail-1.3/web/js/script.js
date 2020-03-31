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
    let token = document.querySelector("#myLink").value;
    if(token=='')
    {
        $('#badInfos').html('<h3>Put your token please !</h3>')
        $('#badInfos').css('display','block');
        $('#myModal').modal('show');
    }
}

$('#badInfos').css('display','none');
$('#goodInfos').css('display','none');