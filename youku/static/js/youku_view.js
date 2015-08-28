/* Javascript for youkuXBlock. */
function youkuXBlockInitView(runtime, element) {
    /* Weird behaviour :
     * In the LMS, element is the DOM container.
     * In the CMS, element is the jQuery object associated*
     * So here I make sure element is the jQuery object */
     //get params from studio
     get_params(runtime, element);
     console.log("mytest");
}
function get_params(runtime, element){
	$.ajax({
            type: "POST",
            url: runtime.handlerUrl(element, 'get_params'),
            data: JSON.stringify({a: 'a'}),
            success: function(result) {
                console.log(result);
                file_id = result.file_id;
                app_id = result.app_id;
                width = result.width;
                height = result.height;
                show_player(file_id,app_id,width,height);
                //watched_status.text(result.watched);
            }
        });

}

function show_player(file_id,app_id,width,height){
     player = new YKU.Player('youkuplayer',{
         styleid: '0',
            client_id: app_id,
            vid: file_id
     });
}
