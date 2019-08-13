;; Auto-generated. Do not edit!


(when (boundp 'gui::waypoints)
  (if (not (find-package "GUI"))
    (make-package "GUI"))
  (shadow 'waypoints (find-package "GUI")))
(unless (find-package "GUI::WAYPOINTS")
  (make-package "GUI::WAYPOINTS"))

(in-package "ROS")
;;//! \htmlinclude waypoints.msg.html


(defclass gui::waypoints
  :super ros::object
  :slots (_p_1 _p_2 _p_3 _p_4 _p_5 ))

(defmethod gui::waypoints
  (:init
   (&key
    ((:p_1 __p_1) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:p_2 __p_2) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:p_3 __p_3) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:p_4 __p_4) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:p_5 __p_5) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _p_1 __p_1)
   (setq _p_2 __p_2)
   (setq _p_3 __p_3)
   (setq _p_4 __p_4)
   (setq _p_5 __p_5)
   self)
  (:p_1
   (&optional __p_1)
   (if __p_1 (setq _p_1 __p_1)) _p_1)
  (:p_2
   (&optional __p_2)
   (if __p_2 (setq _p_2 __p_2)) _p_2)
  (:p_3
   (&optional __p_3)
   (if __p_3 (setq _p_3 __p_3)) _p_3)
  (:p_4
   (&optional __p_4)
   (if __p_4 (setq _p_4 __p_4)) _p_4)
  (:p_5
   (&optional __p_5)
   (if __p_5 (setq _p_5 __p_5)) _p_5)
  (:serialization-length
   ()
   (+
    ;; float32[] _p_1
    (* 4    (length _p_1)) 4
    ;; float32[] _p_2
    (* 4    (length _p_2)) 4
    ;; float32[] _p_3
    (* 4    (length _p_3)) 4
    ;; float32[] _p_4
    (* 4    (length _p_4)) 4
    ;; float32[] _p_5
    (* 4    (length _p_5)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _p_1
     (write-long (length _p_1) s)
     (dotimes (i (length _p_1))
       (sys::poke (elt _p_1 i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _p_2
     (write-long (length _p_2) s)
     (dotimes (i (length _p_2))
       (sys::poke (elt _p_2 i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _p_3
     (write-long (length _p_3) s)
     (dotimes (i (length _p_3))
       (sys::poke (elt _p_3 i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _p_4
     (write-long (length _p_4) s)
     (dotimes (i (length _p_4))
       (sys::poke (elt _p_4 i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _p_5
     (write-long (length _p_5) s)
     (dotimes (i (length _p_5))
       (sys::poke (elt _p_5 i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _p_1
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _p_1 (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _p_1 i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _p_2
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _p_2 (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _p_2 i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _p_3
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _p_3 (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _p_3 i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _p_4
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _p_4 (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _p_4 i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _p_5
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _p_5 (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _p_5 i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get gui::waypoints :md5sum-) "d83cd7bb6bd06c328faaefd30fb67de3")
(setf (get gui::waypoints :datatype-) "gui/waypoints")
(setf (get gui::waypoints :definition-)
      "float32[] p_1
float32[] p_2
float32[] p_3
float32[] p_4
float32[] p_5
")



(provide :gui/waypoints "d83cd7bb6bd06c328faaefd30fb67de3")


