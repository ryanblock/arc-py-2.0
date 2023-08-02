let arc = require('@architect/functions')
exports.handler = arc.http(async req => {
  let { session } = req
  if (session.count == undefined) session.count = 0
  else session.count++
  let json = { ok: true, runtime: `Node.js ${process.version}`, count: session.count }
  return { session, json }
})
