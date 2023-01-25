function timer(){
    /*Change a specific text by id per seconds, in a countdown style*/
    
    var num = document.getElementById("number").value;

    var interval = setInterval(function(){
        if (num >= 1){
            num = num -1;
            document.getElementById("heading1").innerText = num;
        }

        else {
            //clearInterval(interval);
        }

    }
    , 1000)

}
