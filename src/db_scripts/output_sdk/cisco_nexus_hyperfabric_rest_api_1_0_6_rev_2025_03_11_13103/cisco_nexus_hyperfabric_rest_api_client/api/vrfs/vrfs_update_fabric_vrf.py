from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.common_rest_error import CommonRestError
from ...models.models_vrf import ModelsVrf
from ...types import Response


def _get_kwargs(
    fabric_id: str,
    vrf_id: str,
    *,
    body: ModelsVrf,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/fabrics/{fabric_id}/vrfs/{vrf_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommonRestError, ModelsVrf]]:
    if response.status_code == 200:
        response_200 = ModelsVrf.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CommonRestError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CommonRestError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CommonRestError.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = CommonRestError.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = CommonRestError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CommonRestError, ModelsVrf]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fabric_id: str,
    vrf_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsVrf,
) -> Response[Union[CommonRestError, ModelsVrf]]:
    """Update a specific VRF.

     Update a specific VRF in a fabric.

    Args:
        fabric_id (str):
        vrf_id (str):
        body (ModelsVrf): A VRF is a virtual-routing-and-forwarding instance that represents a
            routing table deployed across nodes in the fabric to implement VRF-lite and the ability to
            have multiple routing tables on a single device. A VRF can be associated to multiple VNIs
            configured with an Anycast Gateway SVI.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ModelsVrf]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        vrf_id=vrf_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fabric_id: str,
    vrf_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsVrf,
) -> Optional[Union[CommonRestError, ModelsVrf]]:
    """Update a specific VRF.

     Update a specific VRF in a fabric.

    Args:
        fabric_id (str):
        vrf_id (str):
        body (ModelsVrf): A VRF is a virtual-routing-and-forwarding instance that represents a
            routing table deployed across nodes in the fabric to implement VRF-lite and the ability to
            have multiple routing tables on a single device. A VRF can be associated to multiple VNIs
            configured with an Anycast Gateway SVI.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ModelsVrf]
    """

    return sync_detailed(
        fabric_id=fabric_id,
        vrf_id=vrf_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    fabric_id: str,
    vrf_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsVrf,
) -> Response[Union[CommonRestError, ModelsVrf]]:
    """Update a specific VRF.

     Update a specific VRF in a fabric.

    Args:
        fabric_id (str):
        vrf_id (str):
        body (ModelsVrf): A VRF is a virtual-routing-and-forwarding instance that represents a
            routing table deployed across nodes in the fabric to implement VRF-lite and the ability to
            have multiple routing tables on a single device. A VRF can be associated to multiple VNIs
            configured with an Anycast Gateway SVI.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ModelsVrf]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        vrf_id=vrf_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fabric_id: str,
    vrf_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsVrf,
) -> Optional[Union[CommonRestError, ModelsVrf]]:
    """Update a specific VRF.

     Update a specific VRF in a fabric.

    Args:
        fabric_id (str):
        vrf_id (str):
        body (ModelsVrf): A VRF is a virtual-routing-and-forwarding instance that represents a
            routing table deployed across nodes in the fabric to implement VRF-lite and the ability to
            have multiple routing tables on a single device. A VRF can be associated to multiple VNIs
            configured with an Anycast Gateway SVI.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ModelsVrf]
    """

    return (
        await asyncio_detailed(
            fabric_id=fabric_id,
            vrf_id=vrf_id,
            client=client,
            body=body,
        )
    ).parsed
