
(cl:in-package :asdf)

(defsystem "gui-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "pf" :depends-on ("_package_pf"))
    (:file "_package_pf" :depends-on ("_package"))
  ))