// document.addEventListener("DOMContentLoaded", function() {
//     const carouselInner = document.getElementById('carousel-inner');

//     // Fetch the list of images from the PHP script
//     fetch('get-carousel-images.php')
//         .then(response => response.json())
//         .then(images => {
//             images.forEach((image, index) => {
//                 const carouselItem = document.createElement('div');
//                 carouselItem.classList.add('carousel-item');
//                 if (index === 0) carouselItem.classList.add('active');

//                 const imgElement = document.createElement('img');
//                 imgElement.src = `images/carousel/${image}`; // Use the correct path
//                 imgElement.classList.add('d-block', 'w-100');
//                 imgElement.alt = `Slide ${index + 1}`;

//                 carouselItem.appendChild(imgElement);
//                 carouselInner.appendChild(carouselItem);
//             });
//         })
//         .catch(error => console.error('Error loading images:', error));
// });