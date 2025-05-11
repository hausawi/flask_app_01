import {useState, useEffect} from 'react'
import api from './api'


function App() {
  const [shipments, setShipments] = useState([]);
  const [formData, setFormData] = useState({
    email: '',
    bl_num : '',
    shipper : '',
    is_released : false,
    created_at: ''
  });
  

  const fetchShipments = async ()=> {
    const response = await api.get('/shipments/');
    setShipments(response.data);
  };


  useEffect(() => {
    fetchShipments();
  }, []);


  const handleInputChenge = (event)=> {
    const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
    setFormData({
      ...formData,
      [event.target.name]: value,
    });
  };


  const handleFormSubmit = async (event)=>{
    event.prevenDefault();
    await api.post('/shipments/');
    setFormData({
      email: '',
      bl_num : '',
      shipper : '',
      is_released : false ? "Yes":"No",
      created_at: ''
    });
  };


  return (
    <div>
      <nav className='navbar navbar-dark bg-primary'>
        <div className='container-fluid'>
          <a className='navbar-brand' href='./app.js'>
            Shippping Agent
          </a>
        </div>
      </nav>
      <div className='container'>

        <form onSubmit={handleFormSubmit}>
          <div className='mb-3 mt-3'>
            <label htmlFor='email' className='form-label'>
              Email
            </label>
            <input type='text' name='email' autoComplete='off' className='form-control' id='email' onChange={handleInputChenge} value={formData.email}/>
          </div>

          <div className='mb-3 '>
            <label htmlFor='bl_num' className='form-label'>
              Bill of loading
            </label>
            <input type='text' autoComplete='off' name='bl_num' className='form-control' id='bl_num' onChange={handleInputChenge} value={formData.bl_num}/>
          </div>

          <div className='mb-3 '>
            <label htmlFor='shipper' className='form-label'>
              Shipper:
            </label>
            <input type='text' name='shipper' autoComplete='off' className='form-control' id='shipper' onChange={handleInputChenge} value={formData.shipper}/>
          </div>

          <div className='mb-3 '>
            <label htmlFor='is_released' className='form-label'>
              Is releasd:
            </label>
            <input type='checkbox' name='is_released' autoComplete='off'  id='is_released' onChange={handleInputChenge} value={formData.is_released}/>
          </div>

          <div className='mb-3 '>
            <label htmlFor='created_at' className='form-label'>
              Created at: 
            </label> 
            <input type='text' autoComplete='off' className='form-control' name='created_at' id='created_at' onChange={handleInputChenge} value={formData.created_at}/>
          </div>

          <button type="submit" className='btn btn-primary'>
            Submit
          </button>

        </form>
        <table className='table table-striped tabel-borered table-hover'>
          <thead>
            <tr>
              <th>Email</th>
              <th>Bill of loading</th>
              <th>Shipper</th>
              <th>Is-releasd</th>
              <th>Created At</th>
            </tr>
          </thead>
          <tbody>
            {shipments.map((shipment)=> (
              <tr key={shipment.id}>
                <td>{shipment.email}</td>
                <td>{shipment.bl_num}</td>
                <td>{shipment.shipper}</td>
                <td>{shipment.is_released? "Yes": "No"}</td>
                <td>{shipment.created_at}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )

}

export default App;
