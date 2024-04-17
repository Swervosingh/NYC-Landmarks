import React, { useState } from 'react';
import videoBg from '../assets/waves.mp4';
import './Pictures.css';

function Pictures() {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    image_url: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("/landmarks", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      }
      throw new Error('Failed to add new landmark');
    })
    .then(newLandmark => {
      console.log("New landmark added:", newLandmark);
      // Optionally, you can perform any additional actions after successful addition, such as updating state or displaying a success message
    })
    .catch(error => {
      console.error('Error adding new landmark:', error);
      // Optionally, you can handle errors here, such as displaying an error message to the user
    });
  };

  return (
    <div className="fullscreen-bg">
      <video autoPlay muted loop className="fullscreen-bg__video">
        <source src={videoBg} type="video/mp4" />
      </video>
      <div className="content">
        <h2>Add New Landmarks Here!</h2>
        <div className="form-box">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="name">Name:</label>
              <input type="text" id="name" name="name" value={formData.name} onChange={handleChange} autoComplete="on" />
            </div>
            <div className="form-group">
              <label htmlFor="description">Description:</label>
              <textarea id="description" name="description" value={formData.description} onChange={handleChange} autoComplete="on"></textarea>
            </div>
            <div className="form-group">
              <label htmlFor="image_url">Image URL:</label>
              <input type="text" id="image_url" name="image_url" value={formData.image_url} onChange={handleChange} autoComplete="on" />
            </div>
            <button type="submit">Submit</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Pictures;



// import React, { useState } from 'react';
// import videoBg from '../assets/waves.mp4';
// import './Pictures.css';

// function Pictures() {
//   const [formData, setFormData] = useState("");
  
  

//   const handleChange = (e) => {
//     const { name, value } = e.target.value;
//     setFormData(prevState => ({
//       ...prevState,
//       [name]: value
//     }));
//   };

//   useEffect(() => {
//     fetch("/pizzas")
//       .then((r) => r.json())
//       .then(setPizzas);
//   }, []);


//   const handleSubmit = (e) => {
//     e.preventDefault();
//     // Here you can handle the form submission, for example, send the data to a backend or display it on the page
//     // console.log(formData);
//     // You can add further logic here, such as clearing the form fields after submission
//     setFormData({
//       name: '',
//       description: '',
//       image_url: ''
//     });
//   };

//   return (
//     <div className="fullscreen-bg">
//       <video autoPlay muted loop className="fullscreen-bg__video">
//         <source src={videoBg} type="video/mp4" />
//       </video>
//       <div className="content">
//         <h2>Add New Landmarks Here!</h2>
//         <div className="form-box">
//           <form onSubmit={handleSubmit}>
//             <div className="form-group">
//               <label htmlFor="name">Name:</label>
//               <input type="text" id="name" name="name" value={formData.name} onChange={handleChange} autoComplete="on" />
//             </div>
//             <div className="form-group">
//               <label htmlFor="description">Description:</label>
//               <textarea id="description" name="description" value={formData.description} onChange={handleChange} autoComplete="on"></textarea>
//             </div>
//             <div className="form-group">
//               <label htmlFor="image_url">Image URL:</label>
//               <input type="text" id="image_url" name="image_url" value={formData.image_url} onChange={handleChange} autoComplete="on" />
//             </div>
//             <button type="submit">Submit</button>
//           </form>
//         </div>
//       </div>
//     </div>
//   );
// }

// export default Pictures;
