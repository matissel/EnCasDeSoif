displayMessages = function(){

    msgType = ["danger-alert", "success-alert"]
    for(msg in msgType){
        tag = "#" + msg
        $(tag).fadeTo(2000, 500).slideUp(500, function(){
        $(tag).slideUp(500);}); 
    }

}