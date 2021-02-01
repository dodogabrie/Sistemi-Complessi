      !=================================================
      ! Funzione di main ausiliaria per eventuale debug
      !=================================================
      ! program main
      !     integer              :: s = 100000
      !     real*8               :: a0 = 0.1
      !     real*8               :: x0 = 0.1
      !     real*8               :: y0 = 0.1
      !     call henonmap(s, x0, y0, a0)
      ! end

      ! Per rendere eseguibile in python lanciare il comando (unix):
      ! f2py -c -m henonmap henon.f --fcompiler=gnu95

      subroutine henonmap(n, x, y, a0)
      !========================================
      ! Funzione che crea la mappa di Henon
      ! dati i parametri iniziali 
      !=======================================
          integer                 :: i
          integer, intent(in)     :: n
          real*8, intent(in)      :: a0
          real*8, intent(inout)   :: x(n)
          real*8, intent(inout)   :: y(n)
          do i = 1, size(x)-1
              x(i+1) = x(i)*dcos(a0) - ( y(i) - x(i)*x(i) )*dsin(a0)
              y(i+1) = x(i)*dsin(a0) + ( y(i) - x(i)*x(i) )*dcos(a0)
          enddo
      end subroutine
