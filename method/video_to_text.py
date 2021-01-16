


	






























































if __name__ == '__main__':
	list1 = [
{
	'time_start': '0:0.260',
	'time_end': '0:19.600',
	'text': 'Deep white balance editing this work is by moda fifi and Michael brown when you take a photo a number of processing steps are applied by the cameras, isp hardware to render the original raw sensor image to its final output image, one of the early steps in this color rendering pipeline is white balance which is upper channel scaling.',
	'vid': 0
},
{
	'time_start': '0:19.600',
	'time_end': '0:43.400',
	'text': "If you get white balancing correct at capture time it's difficult to correct in this example, we know a point in the scene that should be wiped, but when we apply the per channel scaling on the camera rendered image, the results are not correct due to the nonlinear processing applied by the camera's isp after white balance, we have shown that having the wrong white balance setting can have adverse effects on tasks such as object classification and semantic segmentation.",
	'vid': 0
},
{
	'time_start': '0:43.400',
	'time_end': '0:55.140',
	'text': 'Last year at cvpr nineteen we presented a data driven solution to this problem in that work we rendered over 60,000 images with the wrong white balance and with the corresponding correct white balance.',
	'vid': 0
},
{
	'time_start': '0:55.440',
	'time_end': '1:13.200',
	'text': 'Given an input image, our solution used a histogram feature to look up similar examples in our data set to computer correction function this year, we have revisited the problem using a deep neural network framework to understand our new framework, we begin by examining an ideal procedure to change the white balance and a camera rendered image.',
	'vid': 0
},
{
	'time_start': '1:13.200',
	'time_end': '1:27.980',
	'text': 'Ideally, we would first like to undo the cameras processing to get back to the UN white balance raw image, we will refer to this UN processing or de rendering with the function f next after we have directed the image we can select a new white balance setting.',
	'vid': 0
},
{
	'time_start': '1:27.980',
	'time_end': '1:54.460',
	'text': 'Finally, we re-render the image with the new white balance setting, we refer to this re-rendering with the function g, we write this entire process as follows where the function f serves to UN process or director, the image and the function g re-processes the image with a new white balance setting, here we use the superscript t to denote the color temperature of the white balance settings note that we will have many g functions, each representing one of the different white balance settings.',
	'vid': 0
},
{
	'time_start': '1:54.460',
	'time_end': '2:46.900',
	'text': "Our dnn's goal is to model the functionality of the functions f and the multiple functions g, we do not however, have to explicitly director and re-render our input image to raw rgb values, instead we can model the functionality of f and g based on a learned representation, this idea LED us to design an encoder decoder framework as follows, we use an encoder network to map images rendered with arbitrary white balance settings, this encoder mimics the function f from the previous slide, we denote the encoder with a lower case f at training time, we have the corresponding patch used by the encoder that has been rendered with a different white balance setting, including the correct white balance that corresponds to an auto white balance, we train a decoder network denoted as lower case g to process the encoder's representation to an image with this white balance setting, we can also train other decoders.",
	'vid': 0
},
{
	'time_start': '2:46.900',
	'time_end': '3:9.940',
	'text': 'Here we show a decoder trained to produce outputs corresponding to a white balance setting of a shade illumination at testing time, we use this encoder, multi decoder framework to process an arbitrary image, the image is encoded with f and then decoded with one of the g decoders, here we show the image process with the decoders for auto white balance incandescent white balance and shade white balance.',
	'vid': 0
},
{
	'time_start': '3:10.020',
	'time_end': '3:25.640',
	'text': 'At testing time, we use the following implementation, the input image is down sampled to have a maximum resolution of 656 pixels and either dimension, we apply our dnn on this down sampled image to get a small output image with the new white balance setting.',
	'vid': 0
},
{
	'time_start': '3:25.640',
	'time_end': '3:37.240',
	'text': 'We then construct a polynomial color mapping function between the two down sampled input and output images, we apply this color mapping function to the full size image to get the final full sized output.',
	'vid': 0
},
{
	'time_start': '3:37.440',
	'time_end': '3:59.500',
	'text': 'This procedure allows us to process large images in a reasonable time in our implementation, we train three decoders, one decoder for auto white balance, another decoder for incandescent also referred to as tungsten white balance that has a color temperature of approximately 3000 calvin a decoder for shade white balance that has a color temperature of 7500 calvin.',
	'vid': 0
},
{
	'time_start': '3:59.500',
	'time_end': '4:17.620',
	'text': 'To produce images with other color temperatures, we simply blend between the outputs of the incandescent and shade white balance, here we show several images that have been captured with the wrong white balance, we process these with our auto white balance setting an incandescent white balance setting a fluorescent white balance setting and a shade setting.',
	'vid': 0
},
{
	'time_start': '4:17.620',
	'time_end': '4:31.480',
	'text': 'Here we compare our results with recent white balance correction methods from cvpr nineteen we have the added benefit of being able to render our image to a different white balance setting, here we compare our results with several image editing software packages.',
	'vid': 0
},
{
	'time_start': '4:31.480',
	'time_end': '4:40.720',
	'text': 'Quantitatively our method performs better than prior methods for auto white balance correction and for rendering to different white balances see our paper for details.',
	'vid': 0
},
{
	'time_start': '4:40.720',
	'time_end': '4:57.460',
	'text': 'We have described an encoder and multi decoder architecture to allow post capture white balance correction and editing of camera rendered images, our approach produces results that are almost visually indistinguishable to what a camera would have rendered at capture time using different white balance settings.',
	'vid': 0
},
{
	'time_start': '4:57.460',
	'time_end': '4:59.260',
	'text': 'Thank you for watching.',
	'vid': 0
}]






	query = 'correct at capture' 

	video_to_text(list1,query)
