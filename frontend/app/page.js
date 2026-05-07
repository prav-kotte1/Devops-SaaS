'use client'

import { useEffect, useState } from 'react'

export default function Home() {
  const [metrics, setMetrics] = useState({
    cpu: 0,
    ram: 0,
    disk: 0,
  })

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws')

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data)
      setMetrics(data)
    }

    return () => ws.close()
  }, [])

  return (
    <div style={{ padding: '40px', fontFamily: 'Arial' }}>
      <h1>DevOps Monitoring Dashboard</h1>

      <div style={{ marginTop: '30px' }}>
        <h2>CPU Usage: {metrics.cpu}%</h2>
        <h2>RAM Usage: {metrics.ram}%</h2>
        <h2>Disk Usage: {metrics.disk}%</h2>
      </div>
    </div>
  )
}