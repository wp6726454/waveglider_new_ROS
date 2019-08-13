// Auto-generated. Do not edit!

// (in-package gui.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class waypoints {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.p_1 = null;
      this.p_2 = null;
      this.p_3 = null;
      this.p_4 = null;
      this.p_5 = null;
    }
    else {
      if (initObj.hasOwnProperty('p_1')) {
        this.p_1 = initObj.p_1
      }
      else {
        this.p_1 = [];
      }
      if (initObj.hasOwnProperty('p_2')) {
        this.p_2 = initObj.p_2
      }
      else {
        this.p_2 = [];
      }
      if (initObj.hasOwnProperty('p_3')) {
        this.p_3 = initObj.p_3
      }
      else {
        this.p_3 = [];
      }
      if (initObj.hasOwnProperty('p_4')) {
        this.p_4 = initObj.p_4
      }
      else {
        this.p_4 = [];
      }
      if (initObj.hasOwnProperty('p_5')) {
        this.p_5 = initObj.p_5
      }
      else {
        this.p_5 = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type waypoints
    // Serialize message field [p_1]
    bufferOffset = _arraySerializer.float32(obj.p_1, buffer, bufferOffset, null);
    // Serialize message field [p_2]
    bufferOffset = _arraySerializer.float32(obj.p_2, buffer, bufferOffset, null);
    // Serialize message field [p_3]
    bufferOffset = _arraySerializer.float32(obj.p_3, buffer, bufferOffset, null);
    // Serialize message field [p_4]
    bufferOffset = _arraySerializer.float32(obj.p_4, buffer, bufferOffset, null);
    // Serialize message field [p_5]
    bufferOffset = _arraySerializer.float32(obj.p_5, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type waypoints
    let len;
    let data = new waypoints(null);
    // Deserialize message field [p_1]
    data.p_1 = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [p_2]
    data.p_2 = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [p_3]
    data.p_3 = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [p_4]
    data.p_4 = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [p_5]
    data.p_5 = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.p_1.length;
    length += 4 * object.p_2.length;
    length += 4 * object.p_3.length;
    length += 4 * object.p_4.length;
    length += 4 * object.p_5.length;
    return length + 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'gui/waypoints';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd83cd7bb6bd06c328faaefd30fb67de3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[] p_1
    float32[] p_2
    float32[] p_3
    float32[] p_4
    float32[] p_5
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new waypoints(null);
    if (msg.p_1 !== undefined) {
      resolved.p_1 = msg.p_1;
    }
    else {
      resolved.p_1 = []
    }

    if (msg.p_2 !== undefined) {
      resolved.p_2 = msg.p_2;
    }
    else {
      resolved.p_2 = []
    }

    if (msg.p_3 !== undefined) {
      resolved.p_3 = msg.p_3;
    }
    else {
      resolved.p_3 = []
    }

    if (msg.p_4 !== undefined) {
      resolved.p_4 = msg.p_4;
    }
    else {
      resolved.p_4 = []
    }

    if (msg.p_5 !== undefined) {
      resolved.p_5 = msg.p_5;
    }
    else {
      resolved.p_5 = []
    }

    return resolved;
    }
};

module.exports = waypoints;
