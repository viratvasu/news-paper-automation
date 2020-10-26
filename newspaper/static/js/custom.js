$(document).ready(function(){
	$('.delete_branch').submit(function(event){
		event.preventDefault();
		$this = $(this)
		formMethod = $this.attr('method')
		formUrl = $this.attr('action')
		formData = $this.serialize()
		$.ajax({
			method:formMethod,
			url:formUrl,
			data:formData,

			success:function(data){
				$this.prev().text("Deleted Successfully").css("background-color","red")
				$this.css("display","none")
			},
			error:function(data){
				console.log('error')
			},

		})
	})
	//For Changing Subscription
	$('.change_subscription').submit(function(event){
		event.preventDefault();
		$this = $(this)
		formMethod = $this.attr('method')
		formUrl = $this.attr('action')
		formData = $this.serialize()
		$.ajax({
			method:formMethod,
			url:formUrl,
			data:formData,

			success:function(data){
				$message = data.message
				if($message == "Add to Subscription")
				{
					$this.text($message).addClass('btn btn-danger')
				}
				else
				{
					$this.text($message).addClass('btn btn-success')
				}
			},
			error:function(data){
				url = data.responseJSON.url
				window.location.href = url;
			},

		})
	})
});
 