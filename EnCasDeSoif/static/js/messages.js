displayMessages = function(){

    msgType = ["danger-alert", "success-alert", "info-alert"]
    msgType.forEach(function(item,index){
        tag = "#" + item
        $(tag).fadeTo(2000, 500).slideUp(500, function(){
        $(tag).slideUp(500);}); 
    })
        
}