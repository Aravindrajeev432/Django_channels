import React, { useEffect,useState } from 'react'
import axios from 'axios';
function Create() {
  const [data, setData] = useState([])

  async function makeBusy(id){
    console.log("makebusy")
    console.log(id)
    await axios.get(`http://127.0.0.1:8000/busy/${id}`).then((res)=>{}).catch((error)=>{})


  }

  async function makeFree(id){
    console.log("Free")
    await axios.get(`http://127.0.0.1:8000/free/${id}`).then((res)=>{}).catch((error)=>{})
  }


  async function getbay(){ 
await axios.get("http://127.0.0.1:8000/chat").then((res)=>{
  console.log(res)
  setData(res.data)
}).catch((error)=>{
  console.log(error)
})
  }


  useEffect(()=>{

getbay();

  },[])

  return (
    <div>


      <div className='container'>
        <div className='row'>

     {data.map((bay_data,index)=>{
      return(<div className='col' key={index}>
        <div>{
          bay_data.id}
          </div>
          <div>
          {
          bay_data.bay_number}
          </div>
          <div>

          {
          bay_data.status}
          <button onClick={(e)=>makeFree(e.target.id)} id={bay_data.id} disabled={bay_data.status==="Free"?true:false}>Free</button>
          <button onClick={(e)=>makeBusy(e.target.id)} id={bay_data.id}  disabled={bay_data.status==="Busy"? true:false}>Busy</button>
          </div>
      </div>)
     })}

          {/* {
            data? <div className='col'></div> :<div className='col'></div>
          } */}

        </div>

      </div>
    </div>
  )
}

export default Create