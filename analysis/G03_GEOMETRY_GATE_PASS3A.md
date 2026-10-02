# G03 Geometry Gate — Pass 3A

## Rationale
Visibility-Polygon steering depends on geometric free-space computation. Geometry must therefore be validated independently before controller performance is measured.

## Implementation
A clean-room deterministic 2-D module now provides:
- ray/segment intersection;
- nearest obstacle hit along a ray;
- visibility-polygon construction using endpoint-angle ray casting;
- polygon area;
- rectangular boundary construction.

The implementation is intentionally small and auditable. It is not copied from the third-party visibility repository discovered during mining.

## Validation scenes
Four hand-checkable cases are registered:
1. 4 x 4 convex rectangle;
2. 6 x 4 convex rectangle;
3. rectangle with an internal vertical occluder;
4. second occlusion scene used for determinism.

The tests require exact wall intersection, approximately exact rectangle area, reduced visible area under occlusion, and deterministic repeated output.

## Scientific boundary
This geometry implementation is benchmark infrastructure, not a claimed contribution and not the Suri et al. visibility algorithm cited by the Vis.-Poly paper. The published controller may consume it because it computes the same required geometric object, but any reproduction report must state this implementation difference.

## Next gate
If CI passes:
1. freeze the geometry test provenance;
2. implement Vis.-Poly slice construction and active-slice selection;
3. test slice area and matching independently;
4. integrate published gain equations;
5. integrate the verified ARC reset selector;
6. run the first literature-derived controller only after all component tests pass.
