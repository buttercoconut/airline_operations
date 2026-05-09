export async function fetchFlightSchedule() {
  const res = await fetch('/api/flights')
  if (!res.ok) throw new Error('Failed to fetch flights')
  return res.json()
}

export async function submitBooking(booking) {
  const res = await fetch('/api/bookings', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(booking)
  })
  if (!res.ok) throw new Error('Booking failed')
  return res.json()
}

export async function submitPassenger(passenger) {
  const res = await fetch('/api/passengers', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(passenger)
  })
  if (!res.ok) throw new Error('Passenger submission failed')
  return res.json()
}
