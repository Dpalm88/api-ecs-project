from flask import Flask, jsonify
import logging, datetime, os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/health', methods=['GET'])
def health():
    app.logger.info('Health check called')
    return jsonify({'status': 'healthy', 'timestamp': str(datetime.datetime.utcnow())})

@app.route('/api/v1/members/<member_id>/status', methods=['GET'])
def member_status(member_id):
    app.logger.info(f'Status check for member: {member_id}')
    if member_id == 'error_test':
        app.logger.error(f'Simulated error for member: {member_id}')
        return jsonify({'error': 'Internal processing error'}), 500
    return jsonify({'memberId': member_id, 'status': 'active', 'identityScore': 742})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)