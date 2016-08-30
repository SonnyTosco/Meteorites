var url = "https://api.nasa.gov/planetary/apod?api_key=41zeG3ddt3LhInMbcIol3Th6nbRPBfOmR8DzaGkz";


$.ajax({
	url: url,
	success: function(result){
		if(result.media_type == "video") {
			$("#apod_img_id").css("display", "none"); 
			$("#apod_vid_id").attr("src", result.url);
		}
		else {
			$("#apod_vid_id").css("display", "none"); 
			$("#apod_img_id").attr("src", result.url);
		}
		$("#reqObject").text(url);
		$("#returnObject").text(JSON.stringify(result, null, 4));  
		$("#apod_explaination").text(result.explanation);
		$("#apod_title").text(result.title);
	}
});