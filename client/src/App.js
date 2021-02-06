import { useEffect, useState } from 'react'
// import logo from './logo.svg';
import axios from 'axios'
import './App.css';

function App() {
  const [resData, setResData] = useState(null)
  useEffect(() => {
    axios.get('http://localhost:8000/api/reporting/order-dev/')
    .then(res => {
      const respData = res.data
      const data = respData.data || []
      setResData(data)
    })
    .catch(err => {
      console.error(err)
    })
  }, [])
  console.log(resData)
  return (
    <div className='app__contaienr'>
      <header className='app__header'>
        <p>
          Order Report
        </p>
      </header>
      <table className='app__table'>
        <thead>
          <tr className='app__head-row'>
            <th className='app__head-cell'>
              Nama Barang
            </th>
            <th className='app__head-cell'>
              Lead Time
            </th>
            <th className='app__head-cell'>
              Std Dev Order
            </th>
            <th className='app__head-cell'>
              Mean Order
            </th>
            <th className='app__head-cell'>
              Std Dev Demand
            </th>
            <th className='app__head-cell'>
              Mean Demand
            </th>
            <th className='app__head-cell'>
              CV Order
            </th>
            <th className='app__head-cell'>
              CV Demand
            </th>
            <th className='app__head-cell'>
              BE
            </th>
            <th className='app__head-cell'>
              Lead Time
            </th>
            <th className='app__head-cell'>
              Parameter
            </th>
            <th className='app__head-cell'>
              Bullwhip Effect
            </th>
          </tr>
        </thead>

        {resData && (
          resData.map(r => (
            <tr className='app__row'>
              <td className='app__cell'>
                {r.nama_barang}
              </td>
              <td className='app__cell'>
                {r.lead_time}
              </td>
              <td className='app__cell'>
                {r.s_order}
              </td>
              <td className='app__cell'>
                {r.mean_order}
              </td>
              <td className='app__cell'>
                {r.s_demand}
              </td>
              <td className='app__cell'>
                {r.mean_demand}
              </td>
              <td className='app__cell'>
                {r.cv_order}
              </td>
              <td className='app__cell'>
                {r.cv_demand}
              </td>
              <td className='app__cell'>
                {r.be}
              </td>
              <td className='app__cell'>
                {r.lead_time}
              </td>
              <td className='app__cell'>
                {r.parameter}
              </td>
              <td className='app__cell'>
                {r.bullwhip_effect}
              </td>
            </tr>
          ))
        )}
      </table>
    </div>
  );
}

export default App;
